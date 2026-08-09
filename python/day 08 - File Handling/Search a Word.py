file=open("notes.txt","r")
x=file.read()
print(x)
n=str(input("enter the word to search: "))
if n in x:
    print("word found")
else:
    print("word not found")
file.close()