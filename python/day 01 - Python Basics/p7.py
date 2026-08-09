# by using operator(swapping of 3 num without temp varble)
a=10
b=20
a=a+b
b=a-b
a=a-b
print("value of a is", a)
print("value of b is", b)



# by using tuple
a=10
b=20
a,b=b,a
print("value of a is", a)
print("value of b is", b)


#user input
a=int(input("enter a value:"))
b=int(input("enter b value:"))
a,b=b,a
print("value of a is", a)
print("value of b is", b)



