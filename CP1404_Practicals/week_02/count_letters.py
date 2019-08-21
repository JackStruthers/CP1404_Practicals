def letter_counter():
    user_string = "Please"
    number_of_letters = 0
    for char in user_string:
        if char.isalpha():
            number_of_letters += 1
    return number_of_letters


print(letter_counter())
