MIN_LENGTH = 4
user_password = input("Please enter your password: ")
while len(user_password) < MIN_LENGTH:
    print("Please enter a password that is at least 4 characters")
    user_password = input("Please enter your password: ")
encrypted_password = len(user_password) * "*"
print(encrypted_password)
