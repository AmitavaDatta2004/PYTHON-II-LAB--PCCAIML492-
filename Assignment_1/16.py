# Question: Write a Python program to read a string from the user and append it into a file.

# Read input string from the user
user_input = input("Enter a string to append to the file: ")

# Open the file in append mode and write the string
with open("data.txt", "a") as file:  # Replace with your file name
    file.write(user_input + "\n")  # Append the user input with a newline

# Expected Outcome:
# If the user enters:
# Hello, Python!
# The content of "data.txt" after execution:
# Hello, Python!
