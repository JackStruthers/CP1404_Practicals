def main():

    min_length = 4
    user_password = get_password(min_length)
    encrypted_password = len(user_password) * "*"
    print(encrypted_password)


def get_password(min_length):
    user_password = input("Please enter your password: ")
    while len(user_password) < min_length:
        print("Please enter a password that is at least 4 characters")
        user_password = input("Please enter your password: ")
    return user_password


main()
