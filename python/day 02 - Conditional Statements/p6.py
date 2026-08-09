marks=int(input("enter the student marks: "))
if marks>=35:
    print("student has passed")
if marks<0 or marks>100:
    print("invaild marks")
else:
    print("student has failed")