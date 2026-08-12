class Vehicle:
    def move(self):
        print("Vehicle is moving")


class Car(Vehicle):
    def move(self):
        print("Car is driving")


class Bike(Vehicle):
    def move(self):
        print("Bike is riding")


c = Car()
b = Bike()

c.move()
b.move()