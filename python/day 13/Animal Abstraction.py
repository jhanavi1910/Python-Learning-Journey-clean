from abc import ABC,abstractmethod
class animal(ABC):
    @abstractmethod
    def eat(self):
        pass
    @abstractmethod
    def move(self):
        pass
class cat(animal):
    def eat(self):
        print("cats is eating")
    def move(self):
        print("cat is moving")
c=cat()
c.eat()
c.move()
