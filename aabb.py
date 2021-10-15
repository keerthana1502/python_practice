ch=input("enter ch = ").strip()
count=1
for i in range(len(ch)-1):
    if(ch[i] == ch[i+1]):
        count+=1
    else:
        print(f"{ch[i]}{count}",end="")
        count=1
print(ch[-1]+str(count),end="")        
        

    

