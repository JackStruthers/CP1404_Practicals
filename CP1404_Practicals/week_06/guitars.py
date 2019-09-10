from week_06.guitar import Guitar


def main():

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

    if guitars:
        guitars.sort()

        for i, guitar in enumerate(guitars, 1):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = "(Vintage)"

            print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(i, guitar.name, guitar.year, guitar.cost,
                                                                      vintage_string))
    else:
        print("No guitars :( Quick, go and buy one!")


main()
