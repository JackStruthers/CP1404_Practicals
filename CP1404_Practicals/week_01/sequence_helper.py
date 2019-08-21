import math

print("What numbers would you like to use")
number_one = int(input("Number 1: "))
number_two = int(input("Number 2: "))
print("(1) Show even numbers from", str(number_one), "-", str(number_two),
      "\n(2) Show odd numbers from", str(number_one), "-", str(number_two),
      "\n(3) Show square numbers from", str(number_one), "-", str(number_one),
      "\n(4) To quit\n")
options = int(input("Select your option: "))

while options != 4:
    if options == 1:
        for i in range(number_one, (number_two + 1)):
            if i % 2 == 0:
                print(i, end=' ')
        print()

    elif options == 2:
        for i in range(number_one, (number_two + 1)):
            if i % 2 == 1:
                print(i, end=' ')
        print()

    elif options == 3:
        for i in range(number_one, (number_two + 1)):
            if (math.sqrt(i)) % 1 == 0:
                print(i, end=' ')
        print()

    else:
        print("Invalid input \n")

    print("(1) Show even numbers from", str(number_one), "-", str(number_two),
          "\n(2) Show odd numbers from", str(number_one), "-", str(number_two),
          "\n(3) Show square numbers from", str(number_one), "-", str(number_one),
          "\n(4) To quit\n")
    options = int(input("Select your option: "))

print("Thanks for using the program")
