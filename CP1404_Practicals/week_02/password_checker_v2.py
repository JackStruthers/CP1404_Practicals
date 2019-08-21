"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password),
                                                           password))


def is_valid_password(password):
    """Determine if the provided password is valid."""
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    count_lower = sum(i.islower() for i in password)
    count_upper = sum(j.isupper() for j in password)
    count_digit = sum(k.isupper() for k in password)
    count_special = sum(password.count(l) for l in SPECIAL_CHARACTERS)
        # TODO: count each kind of character (use str methods like isdigit)
    if count_lower < 1:
        return False
    elif count_upper < 1:
        return False
    elif count_digit < 1:
        return False
    elif count_special < 1:
        return False
    else:
        return True

    # TODO: if any of the 'normal' counts are zero, return False

    # TODO: if special characters are required, then check the count of those
    # and return False if it's zero

    # if we get here (without returning False), then the password must be valid


main()
