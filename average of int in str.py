a="PYnative29@#8496".strip()
sum=0
count=0

for i in a:
    if (i.isdigit()==True):
        b=int(i)
        count=count+1
        sum=sum+b
        avg=sum/count
print(avg)
        
    
