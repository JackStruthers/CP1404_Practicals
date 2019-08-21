import random
SECRET_NUMBER = random.randint(1, 10)

user_number = int(input("Please guess a number between 1 and 10: "))
while user_number != SECRET_NUMBER:
    user_number = int(input("wrong answer, please try again: "))

print("You got it, the answer was", str(SECRET_NUMBER))
