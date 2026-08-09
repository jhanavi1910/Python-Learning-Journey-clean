class circle:
    def __init__(self,radius):
        self.radius=radius
    def display(self):
        area=3.14*self.radius*self.radius
        print("area:" , area)
radius=int(input("enter the radius: "))
c1=circle(radius)
c1.display()