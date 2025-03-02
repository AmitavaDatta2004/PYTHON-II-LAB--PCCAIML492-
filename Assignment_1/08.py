# Question: Write a Python program to merge two files into another.

# Open the first file and read its content
with open("file1.txt", "r") as file1:
    content1 = file1.read()

# Open the second file and read its content
with open("file2.txt", "r") as file2:
    content2 = file2.read()

# Merge contents and write to a new file
with open("merged_file.txt", "w") as merged_file:
    merged_file.write(content1 + "\n" + content2)  # Ensure a newline between contents

# Expected Outcome:
# The contents of "file1.txt" and "file2.txt" will be combined into "merged_file.txt".