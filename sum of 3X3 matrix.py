a=[]
b=[]
c=[]
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
    c.append([])
    for j in range (2):
        c[i].append(int(input("Enter a number = ")))        
for i in range(2):
    result.append([])
    for j in range (2):
        result[i].append(a[i][j]+b[i][j]+c[i][j])
for i in result:
    print(*i)
