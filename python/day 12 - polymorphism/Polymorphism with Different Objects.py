class student():
    def display(self):
        print("student details:")
class teacher():
    def display(self):
        print("teacher details:")
class principal():
    def display(self):
        print("principal details:")
objects=[student(),teacher(),principal()]
for obj in objects:
    obj.display()