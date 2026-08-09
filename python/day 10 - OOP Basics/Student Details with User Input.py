class student: 
    def __init__(self,name,branch,usn): 
        self.name=name
        self.branch=branch
        self.usn=usn
    def display(self):
        print(f"student name is {self.name}")
        print(f"student branch is {self.branch}")
        print(f"student usn is {self.usn}")
name=input("enter the student name: ")
branch=(input("enter the students branch: "))
usn=input("enter the students usn: ")
s1=student(name,branch,usn)
s1.display()