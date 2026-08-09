class claculator:
    def add(self,a,b):
        print("addition",a+b)
    def sub(self,a,b):
            print("subtraction",a-b)
    def multi(self,a,b):
            print("multiplication",a*b)
    def div(self,a,b):
            print("division",a/b)
a=int(input("enter the a value: "))
b=int(input("enter the b value: "))
calc=claculator()
calc.add(a,b)
calc.sub(a,b)
calc.multi(a,b)
calc.div(a,b)
    