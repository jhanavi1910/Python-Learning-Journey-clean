try:
    a = int(input("Enter the a value: "))
    b = int(input("Enter the b value: "))
    print("Result =", a / b)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Please enter valid integers.")

else:
    print("No error occurred.")

finally:
    print("Division completed.")
