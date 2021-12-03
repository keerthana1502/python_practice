def strupr(func):
    def inner():
        str1=func()
        return str1.upper()
    return  inner
def str2(func1):
    def out():
        str1=func1()
        return str1.split()
    return out
@str2
@strupr
def printstr():
    return "good evening"
print(printstr())