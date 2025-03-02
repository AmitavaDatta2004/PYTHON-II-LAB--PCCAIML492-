# Question: Write a Python program to identify the longest line (by length) in a file.

# Open the file and read all lines
with open("input.txt", "r") as file:  # Replace with your file name
    lines = file.readlines()  # Read all lines

# Find the longest line
longest_line = ""
for line in lines:
    if len(line) > len(longest_line):
        longest_line = line

print(f"Longest line in the file: {longest_line.strip()}")

# Expected Outcome:
# If "input.txt" contains:
# Hello World
# Python programming is fun
# Learning new things is exciting
# Output: Longest line in the file: Learning new things is exciting
