text = input("Enter words: ")

words = text.split()

count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

for word, frequency in count.items():
    print(word, ":", frequency)
