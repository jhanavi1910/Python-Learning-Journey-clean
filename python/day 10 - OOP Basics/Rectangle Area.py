class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def display(self):
        area=self.length * self.width
        print(f"area of rectangle is:",area)
length=int(input("enter the length: "))
width=int(input("enter the width: "))
r1=rectangle(length,width)
r1.display()

                
        