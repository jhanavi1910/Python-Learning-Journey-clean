from abc import ABC, abstractmethod
class animal():
    @abstractmethod
    def sound(self):
        print("animal makes sound")
class dog(animal):
    def sound(self):
        print("dog barks")
d=dog()
d.sound()