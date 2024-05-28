# area of Rectangle using class

class rectangle:
    def area(self,l,b):
        return l*b
    
    def perimeter(self,l,b):
        return 2*(l+b)
    
l = int(input("Enter length: "))
b = int(input("Enter breadth: "))
obj = rectangle()
print("Area:",obj.area(l,b))
print("Perimeter:",obj.perimeter(l,b))