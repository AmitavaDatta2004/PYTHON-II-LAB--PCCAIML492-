import csv

def count_rec(filename):
    count = 0  # Initialize counter

    # Open and read the CSV file
    with open(filename, mode="r") as file:
        reader = csv.DictReader(file)  # Read as dictionary
        
        for row in reader:
            if int(row["Score"]) > 80:  # Check if score is greater than 80
                count += 1

    print(f"Number of students with score more than 80: {count}")

# Call function with file name
count_rec("student.csv")
