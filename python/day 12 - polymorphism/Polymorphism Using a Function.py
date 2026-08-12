class cat():
    def sound(self):
        print("cat meows")
class dog():
    def sound(self):
        print("dog barks")
def makes_sound(animal):
    animal.sound()

c=cat()
d=dog()
makes_sound(d)
makes_sound(c)
