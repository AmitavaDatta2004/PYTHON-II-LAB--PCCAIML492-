# Question: Write a Python program to extract numbers from a text file using isdigit().

# Open the file and read its content
with open("sample.txt", "r") as file:
    words = file.read().split()  # Read and split words

# Extract numbers using isdigit()
numbers = [word for word in words if word.isdigit()]

# Print the extracted numbers
print("Extracted numbers:", numbers)

# Expected Outcome:
# If "sample.txt" contains:
# The price is 250 and the discount is 50. Final price: 200.
#
# Output:
# Extracted numbers: ['250', '50', '200']
# Note: The isdigit() method returns True if all characters in a string are digits. 