class A:
    def sum1(self):
        print(5+5)
class B(A):
    def sub1(self):
        print(5-5)
class C(B):
    def mul1(self):
        print(5*5)
        super().__init__()
obj=C()
obj.sum1()
obj.sub1()
obj.mul1()
class A:
    def __init__(self):
        print(5+5)
class B(A):
    def __init__(self):
        super().__init__()
        print(5-5)
class C(B):
    def __init__(self):
        super().__init__()
        print(5*5)
obj=C()