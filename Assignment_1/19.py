# Question: Write a Python program to read the contents of a file in reverse order.

# Open the file and read all lines
with open("sample.txt", "r") as file:  
    lines = file.readlines()  # Read all lines into a list

# Print the lines in reverse order
for line in reversed(lines):
    print(line.strip())

# Expected Outcome:
# If "sample.txt" contains:
# Line 1: Hello World
# Line 2: Python is great
# Line 3: File handling in Python
#
# Output:
# File handling in Python
# Python is great
# Hello World
