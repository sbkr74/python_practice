# calculator using class
class calci:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mult(self,a,b):
        return a*b
    def div(self,a,b):
        return a//b

obj = calci()
print("Addition:",obj.add(7,3))
print("Substraction:",obj.sub(7,3))
print("Multiplication:",obj.mult(7,3))
print("Division:",obj.div(7,3))