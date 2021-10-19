i=1
while(i<=3):
    if (i%3==0):
        i+=3
    print("1)",i)
    i+=1
a=3*1**3
print("2)",a)
b=~4
print("3)",b)
if(9<0)and(0<-9):
    print("Hello")
elif(9>0) or False:
    print("4) good")
else:
    print("bad")
a=True
b=False
c=False
if not a or b:
    print (1)
elif not a or b and c:
    print (2)
elif not a or b or not b and a:
    print ("5)",3)
else:
    print (4)
a="Ocean Academy "
b=13
print("6) Error")
n="ocean"
m="academy"
if n=="Ocean":
    print(n)
elif m=="academy":
    print("9)",m)
else:
    print(n+m)
if 1 and False:
    print("1 is truely!")
else:
    print("10) ???")
n=6
m=0
for i in range(20):
    m+=1
    if (i == n):
        print("11) stop",m)
        break
    else:
        continue
        print("It goes on")
x=10
y=50
if(x**2 == 100 and y<100):
    print(x,y)