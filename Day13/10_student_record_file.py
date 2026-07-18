# Student Record Management using File Handling

name = input("Enter Student Name: ")
marks = input("Enter Marks: ")

file = open("students.txt", "a")

file.write(f"{name} - {marks}\n")

file.close()

print("Student record saved successfully.")
