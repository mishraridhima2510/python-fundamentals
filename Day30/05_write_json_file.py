# Write JSON File

import json

student = {
    "name": "Riya",
    "age": 22
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("Saved Successfully")
