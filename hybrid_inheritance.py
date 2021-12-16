'''class Mom:
    def a(self):
        print("mom")
class Father:
    def b(self):
        print("father")
class Son:
    def c(self):
        print("son")
        self.gender="M"
class Daughter:
    def d(self):
        print("daughter")
        self.gender="F"
obj=Son()
print(obj.gender)'''
class School:
    def a(self):
        print("school")
class Student1(School):
    def b(self):
        print("student1")
class Student2(School):
    def c(self):
        print("student2")
class Student3(Student1,School):
    def d(self):
        print("student3")
obj=Student3()
obj.a()