def func(x):
    y=4
    return lambda z: x+y+z
for i in range(5):
    closure=func(i)
    print("closure ",i+5," = ","closure ",closure(i+5))