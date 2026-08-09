try:
    a = int(input("Enter the a value: "))
    b = int(input("Enter the b value: "))

    print("Division =", a / b)
    print("Addition =", a + b)
    print("Subtraction =", a - b)
    print("Multiplication =", a * b)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Invalid input! Enter only integers.")

else:
    print("Calculation completed successfully.")

finally:
    print("Program ended.")