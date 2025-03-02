# Question: Write a Python program to remove duplicate words in a file.

# Open the file and read the content
with open("input.txt", "r") as file:  # Replace with your file name
    words = file.read().split()  # Read and split words

# Remove duplicates while maintaining order
unique_words = []
for word in words:
    if word not in unique_words:
        unique_words.append(word)

# Write the unique words back to the file
with open("input.txt", "w") as file:
    file.write(" ".join(unique_words))

# Expected Outcome:
# If "input.txt" contains:
# hello world hello python python programming
# After execution, "input.txt" will contain:
# hello world python programming
