a=int(input("Enter no of input = "))
for i in range (a):
    b=int(input("Enter the 1 or 2= "))
    if (b==1):
        class A:
            def odd(self):
                oddInteger=int(input("Enter odd integer = "))
                for i in range (oddInteger*2):
                    if(i%2!=0):
                        print(i)
        obj=A()
        obj.odd()
    if(b==2):
        class B:
            def even(self):
                m = int(input("Enter the number : "))
                for j in range(m * 2):
                    if (j % 2 == 0):
                        print(j)
        obj1=B()
        obj1.even()