l1=[]
l2=[]
for i in range (6):
    b=int(input("Enter number = "))
    l1.append(b)
print(l1)
for i in range (len(l1)):
    min=l1[0]
    for j in l1:
        if j < min:
            min=j
    l2.append(min)
    l1.remove(min)
print("min",l2[0])
print("max",l2[-1])

