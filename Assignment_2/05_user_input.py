import csv

# File name
filename = "details.csv"

# Get number of entries from user
num_entries = int(input("Enter the number of teams to add: "))

# List to store user input data
data = []

# Taking user input using eval() inside a loop
for _ in range(num_entries):
    entry = eval(input("Enter data as a dictionary (e.g., {'Country': 'India', 'Played': 987, 'Won': 513, 'Lost': 424, 'Tied': 9, 'No Result': 41}): "))
    data.append(entry)  # Append the dictionary to the list

# Writing data to CSV using DictWriter
with open(filename, mode="w", newline="") as file:
    fieldnames = ["Country", "Played", "Won", "Lost", "Tied", "No Result"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()  # Writing header
    writer.writerows(data)  # Writing data rows

print("Data has been written successfully!")
