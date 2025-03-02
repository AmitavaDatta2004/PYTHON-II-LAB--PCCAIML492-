# Question: Write a Python program to count the total number of anagrams in a file.

word_dict = {}  # Dictionary to store sorted word patterns
anagram_count = 0

# Open the file and read words
with open("words.txt", "r") as file:  # Replace with your file name
    words = file.read().split()  # Read all words and split into a list

# Group words by their sorted character representation
for word in words:
    sorted_word = "".join(sorted(word))  # Sorting letters to find anagrams
    if sorted_word in word_dict:
        word_dict[sorted_word].append(word)
    else:
        word_dict[sorted_word] = [word]

# Count anagram groups (only those with more than one word)
for group in word_dict.values():
    if len(group) > 1:
        anagram_count += len(group)

print(f"Total number of anagrams in the file: {anagram_count}")

# Expected Outcome:
# If "words.txt" contains:
# listen silent enlist hello world drawer reward
# Output: Total number of anagrams in the file: 5
# (listen, silent, enlist) → 3
# (drawer, reward) → 2