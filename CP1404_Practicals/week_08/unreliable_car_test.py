from week_08.unreliable_car import UnreliableCar


def main():
    car = UnreliableCar("Ford", 100, 50)
    distance = car.drive(40)
    if distance == 0:
        print("Your car broke down!")
    else:
        print("You drove {}KM".format(distance))


main()
