a=int(input("Enter a number = "))
sum=0
for i in a:
    sum=sum+int(i[0])**3
b=int(a)
if(b==sum):
    print(a,"is amstrong number")
else:
    print(a,"is not an amstrong number")
