file=open("sample.txt","r")
x=file.read()
print(x)
count=0
for ch in x:
    if ch in "aeiou":
        count +=1
        print(count)