class conditonals:
    def func(self):
        a=10
        b=20
        if a+b<=30:
            print("total sum is greater than or equal to 30 ")
            if a+b>30:
                print("sum is less than 30")
            else:
                print("greater than 30")
        else:
            if a<b:
                print("b is greater than a")
            else:
                print("a is greater than b")
x=conditonals()
x.func()