def first():
    global a,b,c,d
    a=int(input("Enter a number = "))
    b=int(input("Enter a number = "))
    c=int(input("Enter a number = "))
    d=int(input("Enter a number = "))
    multiples()
    divides()
    print("sum",e+f)
def multiples():
    global e
    e=a*b
    print("Multiple ",e)
def divides():
    global f
    f=c/d
    print("Divide ",f)
first()
