n=int(input("enter a number = "))
sum=0
for i in range (1,n+1):
    sum=sum+i
print(i,end="+")
print(i+1,"=",sum)