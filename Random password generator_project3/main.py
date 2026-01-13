# Random Password Generator
import random
import string


length = int(input("Enter password length: "))

print("\nChoose password type:")
print("1. Letters only")
print("2. Digits only")
print("3. Symbols only")
print("4. Mix of letters, digits, and symbols")

choice = int(input("Enter your choice (" \
": "))


if choice == 1:
    characters = string.ascii_letters
elif choice == 2:
    characters = string.digits
elif choice == 3:
    characters = string.punctuation
elif choice == 4:
    characters = string.ascii_letters + string.digits + string.punctuation
else:
    print("Invalid choice")
    exit()


password = ""
for i in range(length):
    password += random.choice(characters)


print("\nGenerated Password:", password)
