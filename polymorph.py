# class poly:
#     def intro(self):
#         print("it is a parent class poly")
#     def flight(self):
#         print("it is a second stage of poly")
# class morph:
#     def intro(self):
#         print("it is a child class")
#     def flight(self):
#         print("it is a seconf stage in child class")  
# x=poly()
# y=morph()
# for z in(x,y):
#     z.intro()
#     z.flight()

#private access mobifiers acccessing inside  of the class
# class A:
#     def __init__(self):
#         self.__x=30
#     def show(self):
#         print(self.__x)
# b=A()
# b.show(  )

#private access mobifiers acccessing outside of the class

# class A:
#     def __init__(self):
#         self.__x=40  #we can access the private attributes outside the class by using obj._classname__variable
# b=A()
# print(b._A__x)  #this is how we can access private attributes outside of the class 

#file handling 

f=open("Person.py","r") #reading a existing file
print(f.read())

