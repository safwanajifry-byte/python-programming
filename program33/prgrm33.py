class rectangle:
 def __init__(self,length,breadth):
    self.length = length
    self.breadth = breadth
 def area(self):
    return self.length*self.breadth
 def perimeter(self):
    return 2*(self.length+self.breadth)
l1=int(input("enter length 1:"))
b1=int(input("enter breadth 1:"))
r1=rectangle(l1,b1)
print("area of rectangle 1:",r1.area())
print("perimeter of rectangle 1:",r1.perimeter())
l2=int(input("enter length 2:"))
b2=int(input("enter breadth 2:"))
r2=rectangle(l2,b2)
print("area of rectangle2:",r2.area())
print("perimeter of rectangle2:",r2.perimeter())
a1=r1.area()
a2=r2.area()
if a1>a2:
    print("area of rectangle 1 is higher")
elif a1== a2:
    print("area are equal")
else:
    print("area of rectangle 2 is higher")