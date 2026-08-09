marks=int(input("enter the student marks: "))
if marks<0 or marks>100:
    print("invalid marks")
elif marks>=90 and marks<=100:
    print("grade A")
elif marks>=80 :
    print("grade B")
elif marks>=70:
    print("grade C")
elif marks>=60:
    print("grade D")
else:
    print("below average")