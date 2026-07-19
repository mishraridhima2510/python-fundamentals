# File Exception Handling

try:
    file = open("data.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("Data file does not exist.")
