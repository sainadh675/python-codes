class palindrome:
    def __init__(self):
        pass
    def func(self):
        num=int(input("enter the number :"))
        temp=num
        rev=0
        while num>0:
            dig=num%10
            rev=rev*10+dig
            num=num//10
        if temp==rev:
            print("it is a palindrome number")
        else:
            print("it is not a plaindrome number")
x=palindrome()
x.func()