a=input("Enter a number = ")
n=int(a)
sum=0
i=0
while n>0:
    rem=n%10
    sum+=rem
    n=n//10
    if(i<len(a)-1):
        print(a[i],end="+")
    else:
        print(a[i],"=",sum,end="")
    i=i+1
