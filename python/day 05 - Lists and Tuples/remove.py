num=[10,20,22,30,40,16]
print(num)
rem=int(input("enter the element to remove: "))
if rem in num:
    x=num.remove(rem)
    print("element removed")
else :
    print("element not found")
print(num)