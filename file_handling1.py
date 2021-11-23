f=open("demo.txt","w")
l=["apple\n","banana\n","cat\n","dog\n"]
f.write("hello\n")
f.writelines(l)
f.close()