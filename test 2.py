a,b=1,0
a=a^b
b=a^b
a=a^b
print(a)
list=['a','b','c']
list+='de'
print(list)
v=154
while(not(v)):
    v**=2
else:
    v//=2
print(v)
l1=[1,[2,3],4]
l2=l1.copy()
l2[1][1]=7
print(l1,l2)
x=['ab','cd']
for i in x:
    i.upper()
print(x)
sets={3,4,5}
sets.update([1,2,3])
print(sets)
n=5
s=6
a=88
b=77
if a>b:
    for i in range(s):
        b+=n
        if b>100:
            break
        else:
            b=100
b+=n
print(b)
if(n==5):
    print("Hello")
else:
    print("Hai")
s="Hello World"
for i in s:
    print (i)
l=list('123456')
l[0]=l[5]=0
l[3]=l[-2]
print(l)