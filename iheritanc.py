class Person:
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
    def details(self):
        print("my name is: {}".format(self.name))
        print("my id is: {}".format(self.idnumber))
class child(Person):
    def __init__(self,name,idnumber,salary):
        self.salary=salary
        Person.__init__(self,name,idnumber)
    def details(self):
        # print("my name is {}".format(self.name))
        # print("my id is {}".format(self.idnumber))
        super().details()   # super() is used here to take refernce of the parent class method 
        print("my salary is {}".format(self.salary))
name=input("enter the name: ")
idnumber=int(input("enter the id number :"))
salary=int(input("enter the salary :"))
a=child(name,idnumber,salary)
a.details()