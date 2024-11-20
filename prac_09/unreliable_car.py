from prac_09.car import Car
from random import randint


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability: float):
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        return f"{super().__str__()}, reliability = {self.reliability}%"

    def drive(self, distance):
        if self.reliability > randint(0, 100):
            return super().drive(distance)
        else:
            return 0