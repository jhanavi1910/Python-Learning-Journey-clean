from abc import ABC, abstractmethod
class bank(ABC):
    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass
class sbi(bank):
    def deposit(self):
        print("money deposited")
    def withdraw(self):
        print("money withdrawed")
a=sbi()
d=a.deposit()
w=a.withdraw()

