MIN_LENGTH = 4


def main():

    user_password = get_password()
    encrypted_password = encrypt_password(user_password)
    print(encrypted_password)


def encrypt_password(user_password):
    encrypted_password = len(user_password) * "*"
    return encrypted_password


def get_password():
    user_password = input("Please enter your password: ")
    while len(user_password) < MIN_LENGTH:
        print("Please enter a password that is at least 4 characters")
        user_password = input("Please enter your password: ")
    return user_password


main()
