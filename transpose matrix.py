a=[]
result=[]
for i in range (2):
    a.append([])
    for j in range (2):
        a[i].append(int(input("enter a number = ")))
for i in range (2):
    result.append([])
    for j in range(2):
        result[i].append(int(input("Enter a number = ")))        
for i in range (2):
    for j in range (2):
        result[j][i]=a[i][j]
for i in result:
    print(*i)
