a=input("Enter character = ".split(","))
num=int(input("number of words")
for j in range(num):
        b=input("Enter a string = ")        
c=len(a)
count=0
for i in range(len(b)):
    if(b[i] in a):
        count=count+1
        a.remove(b[i])
if(count==(len(b))):        
    print("yes")
else:
    print("no")
