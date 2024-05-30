from abc import ABC,abstractmethod
class parent(ABC):
    @abstractmethod
    def fun(self):
        pass
class child(parent):
    def fun(Self):
        print("abstract method")
x=child()
x.fun()
# f=open("Person.py","r") # file handling to open an already existing class 
# print(f.read())  # read() method is used to read the file