import csv

def make_copy(source_file, target_file):
    # Open source file to read data
    with open(source_file, mode="r") as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + ["Total"]  # Add "Total" column

        # Open target file to write data
        with open(target_file, mode="w", newline="") as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            
            writer.writeheader()  # Write headers
            
            for row in reader:
                # Calculate Total (P + C + M)
                row["Total"] = int(row["P"]) + int(row["C"]) + int(row["M"])
                
                # Write updated row to new file
                writer.writerow(row)

    print(f"File '{target_file}' has been created with total marks added!")

# Call function to create the copy
make_copy("student.csv", "copy.csv")
