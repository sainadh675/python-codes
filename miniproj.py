class Person:
    quote='welcome to Bharat petroleum '
    ending='Thank you'
    def __init__(self,bill_no,fuel_type):
        self.bill_no=bill_no
        self.fuel_type=fuel_type
        
    def details(self):
        print('=============================')
        print(Person.quote)
        print("Bill number is: {}".format(self.bill_no))
        print("Fuel Type is: {}".format(self.fuel_type))

class child(Person):
    def __init__(self,name,idnumber,amount):
        self.amount=amount
        Person.__init__(self,bill_no,fuel_type)
    def details(self):
        # print("my name is {}".format(self.name))
        # print("my id is {}".format(self.idnumber))
        super().details()   # super() is used here to take refernce of the parent class method 
        print(" amount is {}".format(self.amount))
        print(Person.ending)
        print('=============================')

bill_no=int(input("enter the bill number: "))
fuel_type=input("enter the fuel type:")
amount=int(input("enter the amount :"))
a=child(bill_no,fuel_type,amount)
a.details()