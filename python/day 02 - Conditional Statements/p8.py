print("calculator")
print("1. addition")
print("2. subtraction")
print("3. multiplication")
print("4. division")
choice=int(input("enter the choice from 1-4: "))
a=int(input("enter the a value: "))
b=int(input("enter the b value: "))
if choice==1:
    print("result=",a+b)
if choice==2:
    print("result=",a-b)
elif choice==3:
    print("result=",a*b)
else:
    print("result=",a/b)