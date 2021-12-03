print(dir())
num=20
def f1():
    n=10
    print("inside",dir())
f1()
print("outside: ",dir())
def fu():
    print ("hi")
print(fu())
def function():
    print("hello")
g=function
print(g)
g()
def out():
    x=3
    def inn():
        y=3
        res=x+y
        return  res
    return inn
a=out()
print(a())
print(a.__name__)
