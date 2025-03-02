# Question: Write a Python program to count and display the number of vowels in a text file.

# Open first.txt and read content
with open("first.txt", "r") as file:
    text = file.read().lower()  # Read file content and convert to lowercase

# Count vowels in the text
vowels = "aeiou"
vowel_count = sum(1 for char in text if char in vowels)

# Display the count of vowels
print(f"Number of vowels in the file: {vowel_count}")

# Expected Outcome:
# If "first.txt" contains:
# aaaa
# Output:
# Number of vowels in the file: 4
