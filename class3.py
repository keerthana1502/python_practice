class A:
    def __init__(self):
        a=int(input("Enter the number of input : "))
        for i in range (a):
            b=int(input("Enter 1 or 2 : "))
class B(A):
    super().__init__()
    def __init__(self):
        if(self.b==1):
            def __init__(self):
                n=int(input("Enter the number : "))
                for i in range (0,n*n):
                    if(i%2!=0):
                        print(self.i)
        elif(self.b==2):
            def __init__(self):
                n=int(input("Enter the number : "))
                for j in range(0,n*n):
                    if(j%2==0):
                        print(self.j)
obj=B()