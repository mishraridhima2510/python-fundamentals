# Email Uniqueness Checker

emails = set()

while True:
    email = input("Enter Email (type exit to stop): ")

    if email.lower() == "exit":
        break

    if email in emails:
        print("Duplicate Email!")
    else:
        emails.add(email)
        print("Email Added Successfully!")

print("\nUnique Emails:")
for email in emails:
    print(email)
