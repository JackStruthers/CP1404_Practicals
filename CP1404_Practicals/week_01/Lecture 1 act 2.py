def main():

    user_age = int(input("Please enter your age: "))

    while user_age < 0:
        user_age = int(input("You must be older than 0: "))

    if user_age < 18:
        print("You are a child")
    else:
        print("You are an adult")


main()
