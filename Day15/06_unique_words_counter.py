# Count Unique Words

sentence = input("Enter a sentence: ")

words = sentence.lower().split()

unique = set(words)

print("Unique words:", len(unique))
print(unique)
