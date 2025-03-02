# Question: Write a Python program to read specific lines from a file.

# Open the file in read mode
with open("sample.txt", "r") as file:  # Replace with your file name
    lines = file.readlines()  # Read all lines into a list

# Specify the line numbers to read (1-based index)
line_numbers = [1, 3, 5]  # Change these to read different lines

# Read and print the specific lines
for i in line_numbers:
    if 1 <= i <= len(lines):  # Ensure the line number is within range
        print(lines[i - 1].strip())  # Print the line (adjust index for 0-based list)

# Expected Outcome:
# If "sample.txt" contains:
# Line 1: Hello World
# Line 2: Python is great
# Line 3: File handling in Python
# Line 4: Reading specific lines
# Line 5: This is the last line
#
# Output (for line_numbers = [1, 3, 5]):
# Hello World
# File handling in Python
# This is the last line
