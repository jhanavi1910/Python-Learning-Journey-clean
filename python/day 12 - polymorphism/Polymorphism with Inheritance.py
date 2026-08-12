class animal():
    def sound(self):
        print("animal makes sound")
class cat(animal):
    def sound(self):
        print("cat meows")
class dog(animal):
    def sound(self):
        print("dog barks")
d=dog()
c=cat()
d.sound()
c.sound()