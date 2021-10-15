a=int(input("Enter a numer = "))
sum=0
num=a
while(num!=0):
    digit=num%10
    sum=sum+digit**3
    num //=10
if a==sum:
    print(a,"amstrong no")
else:
    print(a,"not amstrong no")
    
    
