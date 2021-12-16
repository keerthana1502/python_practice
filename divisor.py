n=int(input("Enter the number = "))
l=[]
for i in range(1,11):
    if(n%i==0):
        a=l.append(i)
print(max(l))