import csv

# File name
filename = "details1.csv"

# Data to write as a list of dictionaries
data = [
    {"Country": "England", "Played": 746, "Won": 375, "Lost": 334, "Tied": 9, "No Result": 28},
    {"Country": "Australia", "Played": 949, "Won": 575, "Lost": 331, "Tied": 9, "No Result": 34},
    {"Country": "India", "Played": 987, "Won": 513, "Lost": 424, "Tied": 9, "No Result": 41}
]

# Writing data to CSV using DictWriter
with open(filename, mode="w", newline="") as file:
    fieldnames = ["Country", "Played", "Won", "Lost", "Tied", "No Result"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()  # Writing header
    writer.writerows(data)  # Writing data rows

print("Data has been written successfully using dictionary!")
