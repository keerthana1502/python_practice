class Demo:
    def display(self,a=None,b=None,c=None):
        self.a=a
        self.b=b
        self.c=c
        if(self.a!=None and self.b!=None and self.c!=None):
            result=self.a+self.b+self.c
            print(result)
        elif(self.a!=None and self.b!=None):
            result=self.a+self.b
            print(result)
        else:
            result = self.a
            print(result)
obj=Demo()
obj.display(1,2)
