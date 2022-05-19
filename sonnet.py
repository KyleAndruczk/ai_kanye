import re
import pronouncing
import random

### Start of generating rhyming lines 

    # Generate rhyming couplet
def generate_couplet(rhymes):
    while 1:
        i = random.randrange(len(rhymes.keys()))
        if len(rhymes[i]) >= 1:
            pool = rhymes[i] + [i]
            return random.sample(set(pool), 2) 

# Generate 4 rhyming lines
def generate_4lines(rhymes):
    a = generate_couplet(rhymes)
    b = generate_couplet(rhymes)
    return [a[0], b[0], a[1], b[1]]

# Convert 4 lines from index array to string
def conv_4lines(indices, line_dict):
    rhyme_lines = ""
    for i in indices:
        rhyme_lines += line_dict[i] + "\n"
    return rhyme_lines

# Get lines from generated text of each output file

GENERATED_FILES = [i + "_out.txt" for i in START_WORDS]
for files in GENERATED_FILES:

    input_lines = open(files, "r")
    lines = [line.strip() for line in input_lines.readlines()]

# Array of final word of each line
final_words = [re.sub(r'[^\w\s]', '', line.split(" ")[-1]) for line in lines]

# Enumerated dictionaries
line_dict = {i:w for i, w in enumerate(lines)}
word_dict = {i:w for i, w in enumerate(final_words)}

# Rhyming indices
# { 0 : [1, 2, 3] } means that line 0 rhymes with lines 1, 2, 3
rhyme_dict = {}

for i, word1 in word_dict.items():
    # Get potential rhymes from pronouncing package
    potential_rhymes = pronouncing.rhymes(word1)
    rhymes = []
    for x, word2 in word_dict.items():
        # Disallow rhyming with self or same word
        if word1 != word2:
            if word2 in potential_rhymes:
                rhymes.append(x)
    rhyme_dict[i] = rhymes

# Write generated 4-line rhymes to text file
for files in START_WORDS:
    filename = "{0}_rhyme.txt".format(files[:])
    print(files, filename)
    rhyme_file = open(filename, "w+")
    NUM_4LINES = 5
    for i in range(NUM_4LINES):
        rhyme_lines = conv_4lines(generate_4lines(rhyme_dict), line_dict)
        rhyme_file.write(rhyme_lines)
        rhyme_file.write("\n")
    rhyme_file.close()


