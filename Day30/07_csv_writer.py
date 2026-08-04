# CSV Writer

import csv

with open("students.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Name", "Age"])
    writer.writerow(["Rahul", 20])

print("CSV Created")
