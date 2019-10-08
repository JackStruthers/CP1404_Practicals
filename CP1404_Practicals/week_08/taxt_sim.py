from week_08.taxi import Taxi
from week_08.silver_service_taxis import SilverServiceTaxi


def main():
    current_taxi = None
    bill = 0.0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    menu = "q)uit, c)hoose taxi, d)rive"
    print(menu)
    choice = input(">>>").upper()

    while choice != "Q":

        if choice == "C":
            for i, line in enumerate(taxis):
                print("{} - {}".format(i, line))
            current_taxi = int(input("Chose Taxi: "))
            print("Bill to date: ${:.2f}".format(bill))

        if choice == "D":
            distance = int(input("Drive how far? "))
            taxis[current_taxi].drive(distance)
            bill += taxis[current_taxi].get_fare()
            print("Your {} trip cost you ${:.2f}".format(taxis[current_taxi].name, taxis[current_taxi].get_fare()))
            print("Bill to date: ${:.2f}".format(bill))

        print(menu)
        choice = input(">>>").upper()

    print("Total trip cost: ${:.2f}".format(bill))
    print("Taxis are now:")
    for i, line in enumerate(taxis):
        print("{} - {}".format(i, line))


main()
