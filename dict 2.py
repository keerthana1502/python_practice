a="oocccceaaaaaaannnnn"
count=1
for i in range (len(a)):
    if(a[0::]==a[::-1]):
        count=count+1
    else:
        print(a[0]," ",count)
        count=1
print()