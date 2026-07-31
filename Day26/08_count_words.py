# Count Words

with open("sample.txt", "r") as file:
    text = file.read()

words = len(text.split())

print("Total words:", words)
