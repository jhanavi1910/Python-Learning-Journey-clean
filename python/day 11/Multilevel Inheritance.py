class Grandparent:
    def house(self):
        print("Grandparent has a house")


class Parent(Grandparent):
    def car(self):
        print("Parent has a car")


class Child(Parent):
    def bike(self):
        print("Child has a bike")


c = Child()

c.house()
c.car()
c.bike()