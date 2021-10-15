n=int(input("Enter a number = "))
sumof=0
for i in range(1,n):
    if(n%i==0):
        sumof=sumof+i
if(n==sumof):
    print(sumof,"is perfect number")
else:
    print(sumof,"is not perfect number")
        
