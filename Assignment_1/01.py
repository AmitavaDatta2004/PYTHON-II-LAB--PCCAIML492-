# Question: Write a Python program to write multiple lines of text into a file named "mylife.txt".

# Define multiple lines of text to be written to the file
lines = [
    "Dream big, work hard, stay focused.",
    "Consistency is the key to success.",
    "Believe in yourself and never give up."
]

# Open the file in write mode and write the lines
with open("mylife.txt", "w") as file:
    file.writelines("\n".join(lines))  # Join lines with newline characters and write

# Expected Output (Content inside "mylife.txt"):
# Dream big, work hard, stay focused.
# Consistency is the key to success.
# Believe in yourself and never give up.
