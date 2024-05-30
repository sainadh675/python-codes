class Person:
    a=1
    def m1(self):
        self.b=2
        print(Person.a)
        print(self.b)
class y(Person):
    c=3
    def m2(self):
        self.d=4
        print(y.c)
        print(self.d) 
y1=y()
y1.m1()
y1.m2()  
