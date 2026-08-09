try:
    num=[10,20,30,40]
    print(num[3])
except IndexError:
    print("out of range")
else:
    print("in range")
finally:
    print("program ended")