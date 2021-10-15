n=int(input("Enter a number = "))
reverse=0
dig=int(input("Enter the no of digit = "))
for i in range (dig):
    digit = n%10
    reverse=(reverse*10)+digit
    n=n//10
print("reverse no",reverse)

