import random
import string

def password(length):
    char = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(char) for _ in range(length))

length = int(input("Enter the desired length of the password: "))
result = password(length)
print("Generated password:", result)
