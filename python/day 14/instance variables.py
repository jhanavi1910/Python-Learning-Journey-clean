class Student:

    def __init__(self, name, branch):
        self.name = name
        self.branch = branch

    def display(self):
        print("Name:", self.name)
        print("Branch:", self.branch)


student1 = Student("Jhanavi", "AIML")
student2 = Student("Rahul", "CSE")

student1.display()
student2.display()