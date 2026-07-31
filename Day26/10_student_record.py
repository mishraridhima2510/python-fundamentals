# Student Record System

name = input("Enter student name: ")
marks = input("Enter marks: ")

with open("students.txt", "a") as file:
    file.write(f"{name} - {marks}\n")

print("Student record saved successfully.")
