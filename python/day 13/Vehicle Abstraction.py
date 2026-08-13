from abc import ABC , abstractmethod
class vechile(ABC):
    @abstractmethod
    def start(self):
        print("vechile start")
class bike(vechile):
    def start(self):
        print("bike start by kick")
class scooty(vechile):
    def start(self):
        print("scooty start by self")
b=bike()
s=scooty()
b.start()
s.start()