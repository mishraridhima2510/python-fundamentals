# Count words in a file

file = open("sample.txt", "r")

content = file.read()

words = content.split()

print("Total Words :", len(words))

file.close()
