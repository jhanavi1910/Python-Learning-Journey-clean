class person:
    def __init__(self,age,branch):
        self.age=age
        self.branch=branch
class student(person):
    def display(self):
        print(f"student age is {self.age} and branch is {self.branch}")
age=int(input("enter the age: "))
branch=input("enter the branch: ")
s=student(age,branch)
s.display()

                 