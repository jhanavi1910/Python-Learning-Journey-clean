class Father:
    def father_property(self):
        print("Father owns a house")


class Mother:
    def mother_property(self):
        print("Mother owns jewelry")


class Child(Father, Mother):
    def child_property(self): 
        print("Child owns a bicycle")


c = Child()

c.father_property()
c.mother_property()
c.child_property()
