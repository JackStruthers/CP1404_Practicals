from week_06.guitar import Guitar


def main():

    gibson = Guitar("Gibson L-5 CES", 1922, 16035.4)
    new_guitar = Guitar("New Rocker", 2017, 557.89)

    print(gibson, "\n")

    print("Gibson L-5 CES get_age() Expected 97. Got", gibson.get_age())
    print("New Rocker get_age() Expected 2. Got", new_guitar.get_age(), "\n")

    print("Gibson L-5 CES is_vintage() Expected True. Got", gibson.is_vintage())
    print("New Rocker is_vintage() Expected False. Got", new_guitar.is_vintage())


main()
