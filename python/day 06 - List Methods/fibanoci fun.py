def fib (terms):
    a = 0
    b = 1
    for i in range(terms):
        print(a, end=" ")
        temp = a + b
        a = b
        b = temp
terms=int(input("enter the number: "))
fib(terms)


