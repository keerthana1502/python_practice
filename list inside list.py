num=int(input("enter a number"))
a=[]
for i in range (num):
    a.append([])
    for j in range (num):
        b=int(input("Enter a number"))
        a[i].append(b)      
print(a)
