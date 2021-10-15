for i in range (6):
    for j in range (6):
        if(j==0 or i==0 or j==5 or i==3):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()        
