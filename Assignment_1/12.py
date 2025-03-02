# Question: Read "first.txt" and create "second.txt",
# containing only words that start with a lowercase vowel.

# Open first.txt and read content
with open("first.txt", "r") as file:
    words = file.read().split()  # Read words from file

# Filter words that start with a lowercase vowel
vowels = ('a', 'e', 'i', 'o', 'u')
vowel_words = [word for word in words if word.startswith(vowels)]

# Write filtered words to second.txt
with open("second.txt", "w") as file:
    file.write(" ".join(vowel_words))

# Expected Outcome:
# If "first.txt" contains:
# Carry umbrella and overcoat when it rains.
#
# "second.txt" will contain:
# umbrella and overcoat it
