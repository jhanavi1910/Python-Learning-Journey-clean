class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print("Brand:", self.brand)


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def display(self):
        self.show_brand()
        print("Model:", self.model)


c = Car("Toyota", "Innova")
c.display()