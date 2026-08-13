from abc import ABC,abstractmethod
class employee(ABC):
    @abstractmethod
    def salary(self):
        pass
class manager(employee):
    def salary(self):
        print("manager salary is 50,000")
class developer(employee):
    def salary(self):
        print("developer salary is 60,000")
m=manager()
d=developer()
m.salary()
d.salary()