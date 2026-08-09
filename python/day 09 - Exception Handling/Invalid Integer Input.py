try:
    a = int(input("Enter the value of a: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
else:
    print("Value entered successfully.")
finally:
    print("Input process completed.")

