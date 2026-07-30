# Create Dictionary

keys = ["Name", "Age", "City"]
values = ["Ridhima", 19, "Faridabad"]

student = {k:v for k,v in zip(keys, values)}

print(student)
