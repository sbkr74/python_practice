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

class calculator():
    def __init__(self):
        self.n = []
    def add(self,a):
        self.n.append(a)
        return sum(self.n)
    def sub(self,a):
        self.n.append(a)
        return sum(self.n)
    def mult(self,a):
        act = sum(self.n)*a
        self.n.clear()
        self.n.append(act)
        return act
    def div(self,a):
        act = sum(self.n)//a
        self.n.clear()
        self.n.append(act)
        return act
    def result(self):
        return sum(self.n)

obi = calculator()
choice = 1
while choice != 0:
    print("0. Exit")
    print("1. addition")
    print("2. substration")
    print("3. multiplication")
    print("4. division")
    print("5. result")

    choice = int(input("Enter choice: "))

    if choice == 1:
        obi.add(int(input("enter positive number: ")))

    elif choice == 2:
        obi.sub(int(input("enter negative number: ")))

    elif choice == 3:
        obi.mult(int(input("num: ")))

    elif choice == 4:
        obi.div(int(input("num: ")))
    
    elif choice == 5:
        print(obi.result())
    
    elif choice == 0:
        print("exiting")
        break
    else:
        print("Wrong operation!")


