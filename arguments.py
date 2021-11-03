def first():
    a=int(input("Enter a "))
    b=int(input("Enter b "))
    c=int(input("Enter c"))
    d=int(input("Enter d"))
    print(mul(a,b))
    print(div(c,d))
    print((mul(a,b))+(div(c,d)))
def mul(a,b):
    return(a*b)
def div(c,d):
    return(c/d)
first()

