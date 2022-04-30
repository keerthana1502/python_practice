for i in range (5):
    for j in range (5):
        if((i+j)==(5-1)):
            print("1",end=" ")
        elif((i+j)==5):
            print("2",end=" ")
        elif(i+j==5+1):
            print("3",end=" ")
        elif(i+j==5+2):
            print("4",end=" ")
        elif(i+j==5+3):
            print("5",end=" ")
        else:
            print("*",end=" ")
    print()