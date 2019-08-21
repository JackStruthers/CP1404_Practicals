valid_input = False
age = int
while not valid_input:
    try:
        age = int(input("Please enter your age: "))
        if age < 0:
            age = int(input("Age must be >= 0: "))
        else:
            valid_input = True
    except ValueError:
        print("Please enter a number age")

if age % 2 == 0:
    print("Your age is even")
else:
    print("Your age is odd")
