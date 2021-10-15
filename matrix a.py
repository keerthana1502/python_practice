for i in range (5):
    for j in range (5):
        if(i==2 or (i+j)==2 or (j-i)==2 or (j==0 and i>=2) or (j==4 and i>=2)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()        
