def prime(num):

    if num <= 1:
        print("Not a Prime Number")
        return

    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print("Prime Number")
    else:
        print("Not a Prime Number")


num1 = int(input("Enter a number: "))
prime(num1)