import csv

with open("details.csv","r") as file:
    cread=csv.reader(file)
    for row in cread:
        print(row)