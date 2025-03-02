# Question: Write a Python program to calculate the frequency of all words in a file.

# Open the file and read its content
with open("input.txt", "r") as file:  # Replace with your file name
    words = file.read().split()  # Read and split words

# Dictionary to store word frequencies
word_count = {}

# Count occurrences of each word
for word in words:
    word = word.lower().strip(".,!?")  # Convert to lowercase and remove punctuation
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Print word frequencies
for word, count in word_count.items():
    print(f"{word}: {count}")

# Expected Outcome:
# If "input.txt" contains:
# Hello world! Hello Python.
# Output:
# hello: 2
# world: 1
# python: 1
