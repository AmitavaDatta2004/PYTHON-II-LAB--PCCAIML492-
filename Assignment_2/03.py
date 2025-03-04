import csv

r1=['Australia','949','575','331','9','34']
r2=['India','987','513','424','9','41']

with open("details.csv","a",newline="") as file:
    cwrite=csv.writer(file)
    cwrite.writerow(r1)
    cwrite.writerow(r2)