import random

from week_08.car import Car


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        drive_chance = random.randint(0, 100)
        distance_driven = 0
        if drive_chance <= self.reliability:
            distance_driven = super().drive(distance)
        return distance_driven
