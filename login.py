name=input("Enter name = ")
password=input("Enter password = ")
f=open("demo.txt","r+")
for i in f:
    if(i.split()[0]==name and i.split()[1]==password):
        print("already exist");
        break
else:
    f.write(name)
    f.write(" ")
    f.write(password)
    f.write("\n")
    f.close()

