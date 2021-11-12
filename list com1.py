s=[1,56,832,8,97,987]
a=[f'{i} eligible' if i>18 else f'{i} not eligible' for i in s]
print(a)
b=[print("even") if i%2==0 else print("odd") for i in s]
