a="8374717360"
b="sainadh"
print(a.isdigit())
print(b.isdigit())
c="MUTHUKURI"
print(c.lower())
print(b.upper())
print(b.startswith("sai"))
print(c.endswith("KURI"))
x=b.strip()
print("my name is",x,"im from vzm")
print(b.replace("s","S"))


# extended slicing
print(b[1:5])
num=int(input("enter the number: ")) 
if num>1:
    for i in range(2,num):
        if num%i ==0:
            print("it is not a prime number")
        else:
            print("it is a prime number")
        break
else:
    print("not a prime number")