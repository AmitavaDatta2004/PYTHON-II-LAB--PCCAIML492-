# Question: Write a Python program to copy one file into another.

# Open the source file in read mode
with open("source.txt", "r") as source_file:
    content = source_file.read()  # Read the entire content of the source file

# Open the destination file in write mode and copy content
with open("destination.txt", "w") as destination_file:
    destination_file.write(content)  # Write the content to the new file

# Expected Outcome:
# The content of "source.txt" will be copied to "destination.txt".
# The content of "source.txt" and "destination.txt" will be the same.