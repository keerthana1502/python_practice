a=[]
num=4
diagnol1=0
diagnol2=0
for i in range (num):
    a.append([])
    for j in range (num):
        a[i].append(int(input("enter a number = ")))
        if(i==j):
            diagnol1+=a[i][j]
        if(i+j==(num-1)):
            diagnol2+=a[i][j]
print("diagnol1 = ",diagnol1)
print("diagnol2 = ",diagnol2)
print("sum of both diagnols = ",diagnol1+diagnol2)