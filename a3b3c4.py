ch=input("Enter ch = ")
for i in range (0,len(ch)-1,2):
    if(ch[i].isalpha()):
        print((ch[i])*int(ch[i+1]),end="")
    elif(ch[i+1].isalpha()):
        print((ch[i+1])*int(ch[i]),end="")
