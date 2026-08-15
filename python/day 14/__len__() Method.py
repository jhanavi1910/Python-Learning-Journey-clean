class Course:

    def __init__(self, subjects):
        self.subjects = subjects

    def __len__(self):
        return len(self.subjects)


course = Course(["Python", "DBMS", "AI", "Maths"])

print("Number of subjects:", len(course))