bucket=input("enter character = ").split(",")
noofwords=int(input("enter no of word = "))
for i in range (noofwords):
    count=0
    word=input("enter word = ")
    for j in word:
        if j in bucket:
            count=count+1
            bucket.remove(j)
    if(len(word)==count):
        print(word,"= Yes")
    else:
        print(word,"= no")
