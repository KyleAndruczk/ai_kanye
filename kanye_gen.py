import tensorflow as tf

import numpy as np
import os
import time
import re
import pronouncing
import random

#read then decode the kanye text 
text = open('/Users/kyleandruczk/kanye_lyrics.txt', 'rb').read().decode(encoding='utf-8')
vocab = sorted(set(text))

# Map char:index
char2idx = {u:i for i, u in enumerate(vocab)}
# Map index:char
idx2char = np.array(vocab)

# Convert text to integers
text_as_int = np.array([char2idx[c] for c in text])

### Create Training Examples
def split_input_target(chunk):
    input_text = chunk[:-1]
    target_text = chunk[1:]
    return input_text, target_text

seq_length = 100
examples_per_epoch = len(text)//(seq_length+1)

char_dataset = tf.data.Dataset.from_tensor_slices(text_as_int)
sequences = char_dataset.batch(seq_length+1, drop_remainder=True)

# Split sequences into one-offset strings
dataset = sequences.map(split_input_target)

# Break data into shuffled batches of sequences
BATCH_SIZE = 64
BUFFER_SIZE = 10000
dataset = dataset.shuffle(BUFFER_SIZE).batch(BATCH_SIZE, drop_remainder=True)

### Build Model
def build_model(vocab_size, embedding_dim, rnn_units, batch_size):
    model = tf.keras.Sequential([
        tf.keras.layers.Embedding(vocab_size, embedding_dim,
                                  batch_input_shape=[batch_size, None]),
        tf.keras.layers.GRU(rnn_units,
                            return_sequences=True,
                            stateful=True,
                            recurrent_initializer='glorot_uniform'),
        tf.keras.layers.Dense(vocab_size)
    ])
    return model

vocab_size = len(vocab)
embedding_dim = 256
rnn_units = 1024

model = build_model(
        vocab_size = len(vocab),
        embedding_dim = embedding_dim,
        rnn_units = rnn_units,
        batch_size = BATCH_SIZE)

### Train Model
def loss(labels, logits):
    return tf.keras.losses.sparse_categorical_crossentropy(labels, logits, from_logits=True)

model.compile(optimizer="adam", loss=loss)

# Directory where the checkpoints will be saved
checkpoint_dir = './training_checkpoints'

# Name of the checkpoint files
checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt_{epoch}")

checkpoint_callback=tf.keras.callbacks.ModelCheckpoint(
    filepath=checkpoint_prefix,
    save_weights_only=True)

EPOCHS = 50
history = model.fit(dataset, epochs=EPOCHS, callbacks=[checkpoint_callback])

### Generate Text
tf.train.latest_checkpoint(checkpoint_dir)
model = build_model(vocab_size, embedding_dim, rnn_units, batch_size=1)
model.load_weights(tf.train.latest_checkpoint(checkpoint_dir))
model.build(tf.TensorShape([1, None]))
model.summary()

def generate_text(model, start_string):
    len_gen = 40000
    input_eval = [char2idx[s] for s in start_string]
    input_eval = tf.expand_dims(input_eval, 0)

    text = []

    temp = .75

    model.reset_states()
    for i in range(len_gen):
        if (i % 5000 == 0):
            print("{0}/{1}".format(i, len_gen))
        predictions = model(input_eval)
        predictions = tf.squeeze(predictions, 0)
        predictions = predictions / temp 
        predicted_id = tf.random.categorical(predictions, num_samples=1)[-1, 0].numpy()
        input_eval = tf.expand_dims([predicted_id], 0)
        text.append(idx2char[predicted_id])
    return start_string + ''.join(text)

START_WORDS = [u"I can't lose"]
for word in START_WORDS:
    filename = "{0}_out.txt".format(word[:])
    print(word, filename)
    out_text = open(filename, "w+")
    out_text.write(generate_text(model, start_string = word))
    out_text.close()

