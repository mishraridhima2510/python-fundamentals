students = {}

name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")
cgpa = float(input("Enter CGPA: "))

students[roll] = {
    "Name": name,
    "CGPA": cgpa
}

print("\nStudent Records\n")

for roll, details in students.items():
    print("Roll No:", roll)
    print("Name:", details["Name"])
    print("CGPA:", details["CGPA"])
