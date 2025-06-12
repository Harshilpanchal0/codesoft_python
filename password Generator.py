import random
import string

def generate_password(length):
    character = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(character) for _ in range(length))
    return password

try:
    length = int(input("Enter the desired password length: "))

    if length < 6:
        print("Password length should be at least 6 characters.")
    else:
        password = generate_password(length)
        print("Generated Password:", password)

except ValueError:
    print("Please enter a valid Number")
