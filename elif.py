class condition:
    def __init__(self,age):
        self.age=age
    def func(self):
        # age=int(input("enter the age :"))
       # print("age :",self.age)
        if age>=5 and age<=10:
            print("he is a kid")
        elif age>=10 and age<=15:
            print("he is a younger kid")
        elif age>=15 and age<=20:
            print("he is a college student")
        elif age>=20 and age<=30:
            print("he is a employee")
        elif age>=30 and age<=50:
            print("he is a man")
        else:
            print("he is a old man")
age=int(input("enter the age :"))
x=condition(age)
x.func()