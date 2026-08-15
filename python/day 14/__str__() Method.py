class Student:

    def __init__(self, name, branch):
        self.name = name
        self.branch = branch

    def __str__(self):
        return f"{self.name} - {self.branch}"


student = Student("Jhanavi", "AIML")

print(student)