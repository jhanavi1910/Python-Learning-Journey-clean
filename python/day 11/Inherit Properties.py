class person:
    def __init__(self,name):
        self.name=name
class student(person):
    def display(self):
        print(f"student name is {self.name}")
s=student("jaanu")
s.display()

                 