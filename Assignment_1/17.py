# Question: Write a Python program to capitalize the first letter of each word in a file.

# Open the file in read mode and read its content
with open("sample.txt", "r") as file:  # Replace with your file name
    content = file.read()

# Capitalize the first letter of each word
capitalized_content = content.title()

# Open the file in write mode and update the content
with open("sample.txt", "w") as file:
    file.write(capitalized_content)

# Expected Outcome:
# If "sample.txt" contains:
# hello world! python is fun.
#
# After execution, "sample.txt" will contain:
# Hello World! Python Is Fun.
