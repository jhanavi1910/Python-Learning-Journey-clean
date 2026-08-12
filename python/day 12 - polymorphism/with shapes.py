class Circle:
    def area(self):
        print("Area of circle")


class Rectangle:
    def area(self):
        print("Area of rectangle")


def calculate_area(shape):
    shape.area()


c = Circle()
r = Rectangle()

calculate_area(c)
calculate_area(r)