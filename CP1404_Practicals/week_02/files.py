name = input("Please enter your name: ")
name_file = open("names.txt", 'w')
name_file.write(name)
name_file.close()

name_file = open("names.txt", 'r')
print("Your name is", name_file.read())
name_file.close()

number_file = open("numbers.txt", 'r')
addition = 0
for line in number_file:
    addition += int(line)
print(addition)
number_file.close()

number_calc = open("numbers_calc.txt", 'r')
addition = 0
for line in number_calc:
    addition += int(line)
print(addition)
number_calc.close()
