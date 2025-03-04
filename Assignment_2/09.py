import csv

# File name
filename = "Student.csv"

# Number of records to add
num_records = int(input("Enter the number of students: "))

# List to store student records
students = []

# Taking user input using eval() inside a loop
for i in range(num_records):
    student = eval(input(f"Enter details for Student {i+1} as a dictionary (e.g., {{'Rollno': 1, 'Name': 'Sakham', 'Class': 'XII'}}): "))
    students.append(student)  # Append dictionary to the list

# Writing data to CSV using DictWriter
with open(filename, mode="w", newline="") as file:
    fieldnames = ["Rollno", "Name", "Class"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()  # Writing header
    writer.writerows(students)  # Writing data rows

print("\nData has been written successfully! Here are the stored records:\n")

# Reading and displaying the file contents
with open(filename, mode="r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(", ".join(row))  # Display each row
