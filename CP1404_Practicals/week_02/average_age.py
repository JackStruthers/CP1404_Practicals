age = int(input("Please enter the age of a person (use a negative if there are no more people): "))
collective_age = 0
people = 0

while age >= 0:
    people += 1
    collective_age += age
    age = int(input("Please enter the age of a person (use a negative if there are no more people): "))

if people == 0:
    print("Invalid")
else:
    print("The average age of the group is...", collective_age / people)
