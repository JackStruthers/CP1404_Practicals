from week_08.silver_service_taxis import SilverServiceTaxi


def main():
    hummer = SilverServiceTaxi("Hummer", 200, 2)
    print(hummer.drive(18))
    print("${:.2f}".format(hummer.get_fare()))
    print(hummer)


main()
