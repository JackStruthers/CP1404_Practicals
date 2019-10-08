from week_08.taxi import Taxi
from week_08.silver_service_taxis import SilverServiceTaxi


def main():
    current_taxi = None
    bill = 0.0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    menu = "q)uit, c)hoose taxi, d)rive"

    user_option(bill, current_taxi, menu, taxis)


def user_option(bill, current_taxi, menu, taxis):
    print(menu)
    choice = input(">>>").upper()

    while choice != "Q":

        if choice == "C":
            current_taxi = run_c_option(bill, taxis)

        if choice == "D":
            bill = run_d_choice(bill, current_taxi, taxis)

        print(menu)
        choice = input(">>>").upper()

    run_q_choice(bill, taxis)


def run_q_choice(bill, taxis):
    print("Total trip cost: ${:.2f}".format(bill))
    print("Taxis are now:")
    print_taxis(taxis)


def run_d_choice(bill, current_taxi, taxis):
    bill = bill_calculator(bill, current_taxi, taxis)
    print("Your {} trip cost you ${:.2f}".format(taxis[current_taxi].name, taxis[current_taxi].get_fare()))
    show_bill_to_date(bill)
    return bill


def run_c_option(bill, taxis):
    print_taxis(taxis)
    current_taxi = int(input("Chose Taxi: "))
    show_bill_to_date(bill)
    return current_taxi


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
