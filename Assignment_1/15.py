# Question: Write a Python program to remove specific lines from a file.

# Open the file in read mode
with open("sample.txt", "r") as file:  # Replace with your file name
    lines = file.readlines()  # Read all lines into a list

# Specify the line numbers to remove (1-based index)
lines_to_remove = [2, 4]  # Change these to remove different lines

# Remove the specified lines
filtered_lines = [lines[i] for i in range(len(lines)) if (i + 1) not in lines_to_remove]

# Write the updated content back to the file
with open("sample.txt", "w") as file:
    file.writelines(filtered_lines)

# Expected Outcome:
# If "sample.txt" contains:
# Line 1: Hello World
# Line 2: Python is great
# Line 3: File handling in Python
# Line 4: Reading specific lines
# Line 5: This is the last line
#
# After execution (for lines_to_remove = [2, 4]), "sample.txt" will contain:
# Line 1: Hello World
# Line 3: File handling in Python
# Line 5: This is the last line
