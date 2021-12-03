def func(fu):
    def mul():
        a=fu()
        return a*4
    return  mul
def dunc1(fu1):
    def squ():
        b=fu1()
        return b*10
    return squ
@dunc1
@func
def ans():
    return 10
print(ans())