class Duck:
    def walk(self):
        print("Duck is walking")


class Person:
    def walk(self):
        print("Person is walking")


def start_walking(obj):
    obj.walk()


d = Duck()
p = Person()

start_walking(d)
start_walking(p)