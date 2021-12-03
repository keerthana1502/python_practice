class Student:
    def __init__(self):
        self.rollno=input("Enter the roll no :")
        self.name=input("Enter the name : ")
class Mark(Student):
    def __init__(self):
        super().__init__()
        self.phy=int(input("Phy mark = "))
        self.chem=int(input("Chem mark = "))
        self.maths=int(input("Maths mark = "))
        print("rollno = ", self.rollno)
        print("name = ", self.name)
class Total(Mark):
    def __init__(self):
        super().__init__()
        result=self.phy+self.chem+self.maths
        avg=(result/300)*100
        print("TOTAL = ",result)
        print("AVG = ",avg,"%")
obj=Total()