# Local Chat System

users = []

while True:

    name = input("Enter username (exit to quit): ")

    if name.lower() == "exit":
        break

    users.append(name)

print("\nConnected Users:")

for user in users:
    print(user)

print("\nChat system closed.")
