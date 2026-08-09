class Parent:
    def display(self):
        print("This is the parent class")


class Child(Parent):
    def display(self):
        super().display()
        print("This is the child class")


c = Child()
c.display()
