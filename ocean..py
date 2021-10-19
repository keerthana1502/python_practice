a=input("Enter = ")
for i in range (len(a)):
    for j in range (len(a)):
        if(i==j or j==4-i):
            print(a[j],end="")
        else:
            print(" ",end="")
    print()