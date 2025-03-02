# Question: Write a Python program to check whether two files are identical or not.

# Open both files and read their contents
with open("file1.txt", "r") as file1, open("file2.txt", "r") as file2:
    content1 = file1.read()
    content2 = file2.read()

# Compare the contents of the two files
if content1 == content2:
    print("The files are identical.")
else:
    print("The files are different.")

# Expected Outcome:
# If both files have the same content, it prints: "The files are identical."
# Otherwise, it prints: "The files are different."
