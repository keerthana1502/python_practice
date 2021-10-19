a=[[1,["ocean","pondy","2"]],[2,["xxx","yyy","zzz"]]]
user = ["name","place","age"]
b={}
for i in range(len(a)):
    for j in range(len(a[i])-1):
        b.update({a[i][j]:a[i][j+1]})
print(b)
c=int(input("enter a number = "))
answer = b[c]
for i in range(len(answer)):
    print(user[i],":",answer[i])