n=12345
while(n!=0):
    rem=n%10
    print(rem,end="")
    n=n//10
n=5
for i in range (n+1):
    for j in range (i):
        print("*",end="")
    print()