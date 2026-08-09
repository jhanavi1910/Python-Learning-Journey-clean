try:
    file=open("jhanu.txt","r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("file not found")
else:
    print("file opened sucessfully ")
finally:
    print("program ended")
