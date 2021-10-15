for i in range(5):
    for j in range(5):
        if(i==j or j==5-1-i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()    

