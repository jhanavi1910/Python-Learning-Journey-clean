class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print (f"student name is {self.name} and age is {self.age}")
s=student("jhanavi",20)
s.display()

