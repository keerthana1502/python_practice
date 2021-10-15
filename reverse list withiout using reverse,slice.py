a=[10,20,30,40,50]
length=len(a)
for i in range (length//2):
    n=a[i]
    a[i]=a[length-i-1]
    a[length-i-1]=n
print(a)    
