# Swap Keys and Values

student = {
    "Name": "Ridhima",
    "Branch": "CSE",
    "Year": 2
}

swapped = {value: key for key, value in student.items()}

print(swapped)
