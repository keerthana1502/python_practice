def test():
    n=int(input("Enter the no of input = "))
    for i in range (n):
        m=input(" ").split()
    name = input("Enter the name : ")
    if(m[0]==name):
        avg=(int(m[1])+int(m[2])+int(m[3]))/3
        print("{:.2f}".format(avg))
test()

