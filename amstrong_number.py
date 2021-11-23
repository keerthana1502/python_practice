a=int(input("Enter a numer = "))
sum=0
num=a
while(num!=0):
    digit=num%10
    sum=sum+digit**3
    num //=10
if a==sum:
    print(a," is amstrong no")
else:
    print(a,"is not amstrong no")
    
    
