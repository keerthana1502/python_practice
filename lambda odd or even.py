
y=lambda *b:sum(b)
print(y(1,2,3))
z=lambda **c:sum(c.values())
print(z(one=1,two=2,three=3))