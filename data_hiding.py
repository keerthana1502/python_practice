class A:
    a=5
    _b=6
    __c=7
    def __init__(Self):
        print(Self.a)
        print(Self._b)
        print(Self.__c)
class B(A):
    def __init__(Self):
        super().__init__()
        print(Self.a)
        print(Self._b)
class C(B):
    def __init__(self):
        super().__init__()
        print(self._b)
obj=C()
