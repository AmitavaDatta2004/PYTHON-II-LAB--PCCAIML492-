# Question: Write a Python program to identify the longest word (by length) in a file.

# Open the file and read the content
with open("input.txt", "r") as file:  # Replace with your file name
    words = file.read().split()  # Read and split words

# Find the longest word
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print(f"Longest word in the file: {longest_word}")

# Expected Outcome:
# If "input.txt" contains:
# Python programming is amazing
# Output: Longest word in the file: programming
