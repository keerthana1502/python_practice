list1=['ocean','ocean and sea','blue and black']
a=list(filter(lambda a: ("and" in a),list1))
print(a)