string=input("enter a string = ".strip())
char=input("Enter a char = ")
count=0
for i in string:
    if (i==char):
        count=count+1
print("count if char = ",count)
