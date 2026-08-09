class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)


brand = input("Enter car brand: ")
model = input("Enter car model: ")
year = int(input("Enter year: "))

car1 = Car(brand, model, year)
car1.display()