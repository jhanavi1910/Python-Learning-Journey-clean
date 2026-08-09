try:
    a=int(input("enter the a value: "))
    b=int(input("enter the a value: "))
    print(a/b)
except ZeroDivisionError:
    print("cannot divide by zero ")
except ValueError:
    print("integers cannot be divided")
else:
    print("no error")
finally:
    print("division completed")



   
