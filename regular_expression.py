import re
a="hello world"
x=re.findall("he..o",a)
print(x)
y=re.findall("[a-z]",a)
print(y)
z=re.findall("^h",a)
print(z)
b=re.findall("d$",a)
print(b)
c=re.findall("h.*o",a)
print(c)
d=re.findall("h.+o",a)
print(d)
e=re.findall("h.?",a)
print(e)
f=re.findall("h.{3}o",a)
print(f)
g=re.findall("hello/world",a)
print(g)
h=re.findall("\Ah",a)
print(h)
i=re.findall("\Bd",a)
print(i)
j=re.findall("\Bl",a)
print(j)