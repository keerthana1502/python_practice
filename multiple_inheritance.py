class A:
    def father(self):
        print("class A")
        super().father()
class B:
    def father(self):
        print("class B")
class C(A,B):
    def son(self):
        print("Class C")
obj=C()
obj.father()