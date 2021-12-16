'''a=[1,2,3,4]
n=len(a)
r=int(input("r : "))
import math
b=(math.factorial(n))/(math.factorial(n-r))
print(b)'''

from itertools import permutations
l=[1,2,3]
print(list(permutations(l)))
print(list(permutations(l,1)))
print(list((l,3)))