numbers = []
LIMIT = 5
for i in range(LIMIT):
    values = int(input("Number: "))
    numbers.append(values)

print("The first number is: {}".format(numbers[0]))
print("The last number is: {}".format(numbers[-1]))
print("The smallest number is: {}".format(min(numbers)))
print("The largest number is: {}".format(max(numbers)))
print("The average of the numbers is: {:.1f}".format((sum(numbers))/LIMIT))

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username_select = input("Please enter your user name")

if username_select in usernames:
    print("Access granted")
else:
    print("Access denied")
