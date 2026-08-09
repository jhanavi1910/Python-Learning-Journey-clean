class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def nameage(self):
        print(f"{self.name} is {self.age}")
n1=student("jhanavi",20)
n2=student("disha",21)

n1.nameage()