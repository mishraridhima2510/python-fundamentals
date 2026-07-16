attendance = {"Prateek", "Divya", "Ridhima"}

name = input("Enter student name: ")

if name in attendance:
    print(name, "is Present.")
else:
    print(name, "is Absent.")
