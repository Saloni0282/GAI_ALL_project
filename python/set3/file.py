# Define the input and output file names
input_filename = "input.txt"
output_filename = "output.txt"

# Read the contents of the input file
try:
    with open(input_filename, "r") as input_file:
        content = input_file.read()
except FileNotFoundError:
    print(f"Error: The file '{input_filename}' was not found.")
    exit(1)

# Split the content into words and count them
words = content.split()
word_count = len(words)

# Write the word count to the output file
with open(output_filename, "w") as output_file:
    output_file.write(f"Number of words: {word_count}")

print(f"Number of words: {word_count} (written to '{output_filename}')")
