num=[]
for i in range(5):
    n=int(input("enter the n alue: "))
    num.append(n)
search=int(input("enter the element to search: "))
if search in num:
    print("element found")
else:
    print("element not found")