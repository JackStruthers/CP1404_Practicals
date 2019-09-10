from week_06.guitar import Guitar

guitars = []

"""
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    guitars.append(Guitar(name, year, cost))
    name = input("Name: ")
"""

guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

for i, guitar in enumerate(guitars, 1):
    vintage_string = True if guitar.get_age() >= 50 else False
    if vintage_string:
        vintage_string = "(Vintage)"
    else:
        vintage_string = ""

    print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(i, guitar.name, guitar.year, guitar.cost, vintage_string))
