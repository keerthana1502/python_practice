class A:
    def value(self):
        self.a=20
        self.b=10
class B:
    def sum(self):
        self.z=self.a+self.b
class C:
    def sub(self):
        self.x=self.a-self.b
o=B()
class Teacher:
    def writing(self):
        print("Write")
class S1(Teacher):
    def read(self):
        print("read")
class S2(Teacher):
    def reading(self):
        print("Reading")
obj=S1()
obj.writing()