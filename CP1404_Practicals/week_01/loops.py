for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 110, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

stars = int(input("Please enter the amount of rows you would like: "))
for i in range(stars):
    star_string = (i + 1) * "*"
    print(star_string)
print()

for i in range(stars):
    star_string = (stars - i) * "*"
    print(star_string)
