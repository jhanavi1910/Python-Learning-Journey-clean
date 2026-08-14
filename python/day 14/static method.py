class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b


print("Addition:", Calculator.add(20, 10))
print("Subtraction:", Calculator.sub(20, 10))