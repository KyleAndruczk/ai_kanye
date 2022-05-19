from big_phoney import BigPhoney
import os

def write_iambic(input_file, output_file):
    for line in input_file.readlines():
        syllables = phoney.count_syllables(line)
        if (syllables == 10):
            output_file.write(line)

# Initialization
phoney = BigPhoney()
output_file = open("iambic.txt", "a")
text = "Damn, your lips very sof_out.txt" 




def createIamb(filename):
    print("creating an Iamb using " + filename)
    input_file = open(filename, "r+")
    write_iambic(input_file, output_file)
    input_file.close()

    output_file.close()

createIamb(text)