mylist=[1,2,3,4,5,6]
mylist=list(filter(lambda a: (a%2==0) , mylist))
new_tuple=tuple(filter(lambda a: (a%2==0) , mylist))
new_set=set(filter(lambda a: (a%2==0) , mylist))
print(mylist)
print(new_tuple)
print(new_set)