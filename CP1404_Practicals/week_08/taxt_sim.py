from week_08.taxi import Taxi
from week_08.silver_service_taxis import SilverServiceTaxi


def main():
    current_taxi = None
    bill = 0.0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    menu = "q)uit, c)hoose taxi, d)rive"
    print(menu)
    choice = input(">>>").upper()

    user_option(bill, choice, current_taxi, menu, taxis)


def user_option(bill, choice, current_taxi, menu, taxis):
    while choice != "Q":

        if choice == "C":
            print_taxis(taxis)
            current_taxi = int(input("Chose Taxi: "))
            show_bill_to_date(bill)

        if choice == "D":
            bill = bill_calculator(bill, current_taxi, taxis)
            print("Your {} trip cost you ${:.2f}".format(taxis[current_taxi].name, taxis[current_taxi].get_fare()))
            show_bill_to_date(bill)

        print(menu)
        choice = input(">>>").upper()
    print("Total trip cost: ${:.2f}".format(bill))
    print("Taxis are now:")
    print_taxis(taxis)


def show_bill_to_date(bill):
    print("Bill to date: ${:.2f}".format(bill))


def print_taxis(taxis):
    for i, line in enumerate(taxis):
        print("{} - {}".format(i, line))


def bill_calculator(bill, current_taxi, taxis):
    distance = int(input("Drive how far? "))
    taxis[current_taxi].drive(distance)
    bill += taxis[current_taxi].get_fare()
    return bill


main()
