a=[3,57,83,24,7,9,322,1,5]
b=[]
while a:
    m=a[0]
    for x in a:
        if x < m:
            m=x
    b.append(m)
    a.remove(m)
print(b)
        
