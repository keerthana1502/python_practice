a=int(input("Enter the input = "))
sum=0
for i in range(a):
    n=int(input("Enter the number = "))
    while(n>0):
        rem=n%10
        sum=sum+rem
        n=n//10
    print(sum)
