# Question: Write a Python program to read lines from "diary.txt" 
# and display only those lines which start with the alphabet 'P'.

# Open the file and read all lines
with open("diary.txt", "r") as file:  # Open the file in read mode
    lines = file.readlines()  # Read all lines

# Iterate through each line and print only those starting with 'P'
for line in lines:
    if line.strip().startswith("P"):  # Check if the line starts with 'P'
        print(line.strip())  # Print the line without extra spaces

# Expected Outcome:
# If "diary.txt" contains:
# Python is a great language.
# Java is also popular.
# Programming is fun.
# People love coding.

# Output:
# Python is a great language.
# Programming is fun.
# People love coding.
