a=int(input("input : "))
for k in range(a):
    b=int(input("Enter the value : "))
    if(b==1):
        def odd():
            n=int(input("Enter the number : "))
            for i in range (n*2):
                if(i%2!=0):
                    print(i)
        odd()
    if(b==2):
        def even():
            m=int(input("Enter the number : "))
            for j in range (m*2):
                if(j%2==0):
                    print(j)
        even()