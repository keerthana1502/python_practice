n=int(input("Enter a number = "))
a=n
sumof=0
b=str(n)
c=len(b)
for i in range (n):
    dig=n%10
    sumof=sumof+(dig**c)
    n=n//10
if(a==sumof):
    print("it is an amstrong number")
else:
    print("it is not amstron number")
    
    
    

