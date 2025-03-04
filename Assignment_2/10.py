import csv

filename = "Student.csv"

# Take user input as a list using eval()
row_to_delete = eval(input("Enter the row to delete as a list (e.g., ['3', 'Irfan', 'XII']): "))

# Read data from the CSV file
rows = []
with open(filename, mode="r") as file:
    reader = csv.reader(file)
    header = next(reader)  # Store header separately
    for row in reader:
        if row != row_to_delete:  # Skip the row to be deleted
            rows.append(row)

# Write back to CSV without the deleted row
with open(filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header)  # Write header
    writer.writerows(rows)  # Write remaining data

print(f"\nRecord {row_to_delete} has been deleted (if it existed).")
