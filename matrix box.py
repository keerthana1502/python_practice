n=int(input("Enter "))
for i in range (n):
    for j in range (n):
        if(i==0 or j==0 or i==4-1 or j==4-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()        
