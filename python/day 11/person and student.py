class Person:
    def display_name(self):
        print("Name: Jhanavi")


class Student(Person):
    def display_branch(self):
        print("Branch: AIML")


s = Student()

s.display_name()
s.display_branch()