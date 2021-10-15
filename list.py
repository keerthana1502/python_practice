a=input("Enter string = ")
b=input("enter char = ")
c=[]
for i in a.split():
    if i.startswith(b):
        c.append(i)
print(c)

