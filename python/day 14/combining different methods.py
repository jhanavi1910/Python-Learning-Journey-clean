class Student:

    college = "ABC College"

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Student:", self.name)

    @classmethod
    def show_college(cls):
        print("College:", cls.college)

    @staticmethod
    def welcome():
        print("Welcome to the college")


student = Student("Jhanavi")

student.display()
Student.show_college()
Student.welcome()