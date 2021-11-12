mylist=[1,2,3,4,5,6]
new_list=list(filter(lambda a: (a%2==0) , mylist))
print(new_list)