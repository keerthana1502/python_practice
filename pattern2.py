n=int(input("Enter no "))
for i in range (1,n+1):
    for j in range(1,2*i):
        if(i>j):
            print(j,end=" ")
        elif(i<=j):
            x=(2*i)-j
            print(x,end=" ")
        else:
            print(" ",end=" ")
    print()