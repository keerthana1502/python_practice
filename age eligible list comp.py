s=[36,56,8,9,23,18,57]
list=[f"{i} eligible to vote" if i>=18 else f"{i} not eligible" for i in s]
print(list)
print("hai") if 1>2 else print("hello")
b=[1,2,3,4]
list=["yes" if i==1 else 'no' if i==2 else 'idle' for i in b]
print(list)