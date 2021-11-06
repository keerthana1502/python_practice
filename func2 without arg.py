def inputt():
    global a
    a=int(input("Enter a number = "))
    square()
def square():
    print("square ",a*a)
    cube()
def cube():
    print("cube ",a*a*a)
inputt()
