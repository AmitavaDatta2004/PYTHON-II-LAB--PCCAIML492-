# Question: Write a Python program to delete words at even positions in a line of a file.

# Open the file in read mode
with open("sample.txt", "r") as file:
    lines = file.readlines()  # Read all lines into a list

# Modify each line to remove words at even positions
modified_lines = []
for line in lines:
    words = line.split()  # Split the line into words
    filtered_words = words[::2]  # Keep only words at odd positions
    modified_line = " ".join(filtered_words)  # Join back into a string
    modified_lines.append(modified_line)

# Write the modified content back to the file
with open("sample.txt", "w") as file:
    file.writelines("\n".join(modified_lines))

# Expected Outcome:
# If "sample.txt" contains:
# Python is a great programming language
# Learning new things is always fun
#
# After execution, "sample.txt" will contain:
# Python great language
# Learning is fun
