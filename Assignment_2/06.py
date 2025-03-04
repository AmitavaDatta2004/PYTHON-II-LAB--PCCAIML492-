import csv

# File name
filename = "login_credentials.csv"

# Number of records to add
num_records = 3

# List to store user input
data = []

# Taking user input using eval() inside a loop
for i in range(num_records):
    entry = eval(input(f"Enter details for User {i+1} as a dictionary (e.g., {{'Username': 'john_doe', 'Password': 'john123'}}): "))
    data.append(entry)  # Append dictionary to the list

# Writing data to CSV using DictWriter
with open(filename, mode="w", newline="") as file:
    fieldnames = ["Username", "Password"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()  # Writing header
    writer.writerows(data)  # Writing data rows

print("\nData has been written successfully! Here are the stored credentials:\n")

# Reading and displaying the file contents
with open(filename, mode="r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(", ".join(row))  # Display each row
