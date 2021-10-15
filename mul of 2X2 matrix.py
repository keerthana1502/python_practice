a=[]
b=[]
result=[]
for i in range (2):
    a.append([])
    for j in range (2):
        a[i].append(int(input("Enter a number = ")))
for i in range (2):
    b.append([])
    for j in range (2):
        b[i].append(int(input("Enter a number = ")))
for i in range (2):
    result.append([])
    for j in range(2):
        result[i].append(int(input("Enter a number = ")))      
for i in range (2):
    for j in range(2):
        for k in range (2):
            result[i][j]+=a[i][k]*b[k][j]
for r in result:
    print(*r)
