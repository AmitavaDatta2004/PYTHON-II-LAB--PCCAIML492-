# Question: Write a Python program to read lines from "INDIA.TXT" 
# and display the occurrence of the word 'India'.

count = 0  # Initialize count

# Open the file in read mode
with open("INDIA.TXT", "r") as file:
    for line in file:  # Read line by line
        words = line.split()  # Split line into words
        count += words.count("India")  # Count occurrences of 'India' in the line

print(f"Occurrences of 'India': {count}")

# Expected Output:
# If "INDIA.TXT" contains:
# India is the fastest-growing economy.
# India is looking for more investments around the globe.
# The whole world is looking at India as a great market.
# Most of the Indians can foresee the heights that India is capable of reaching.
#
# Output:
# Occurrences of 'India': 4
