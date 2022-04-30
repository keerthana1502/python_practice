'''n=int(input("enter input : "))
for i in range (1,n+1):
    for j in range(i-1,n):
        print(j*2+1,end=" ")
    for k in range(0,i-1):
        if (k > 9):
            break
        print(k*2+1,end=" ")
    if(i>9):
        break
    print()

rows=int(input("Enter : "))
i = 1
while(i <= rows):
    j = i - 1
    while(j < rows):
        print(j * 2 + 1, end = ' ')
        j = j + 1
    k = 0
    while(k < i - 1):
        print(k * 2 + 1, end = ' ')
        k = k + 1
    print()
    i = i + 1'''
for i in range(1,10,2):
    for j in range(i,10,2):
        print(j,end=" ")
    for k in range(i,15,2):
        print(k+4,end=" ")
        if(k==11):
            break
    print()