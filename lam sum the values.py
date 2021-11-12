y = lambda *b: sum(b)
print(y(1, 2, 3))




z=lambda **c:sum(c.values())
print(z(one=1,two=2,three=3))

x=lambda a,*,b=9,c=0:a+b+c
print(x(2,b=13,c=7))
s=list(map(trace(lambda x: x*2), range(3)))
print(s)