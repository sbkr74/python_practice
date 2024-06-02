# Append,delete and display List using class.
class perform:
    lyst = []
    def add(self,ele):
        self.lyst.append(ele)
        return self.lyst
    
    def delete(self,ele):
        self.lyst.remove(ele)
        return self.lyst
    
    def dis(self):
        for ele in self.lyst:
            print(ele)
        
    
obj = perform()
obj.add('sam')
obj.add('curran')
obj.delete('sam')
obj.dis()

# print("List: ",obj.add('sam'))
# print("List: ",obj.add('curran'))
# print("List: ",obj.delete('sam'))
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class listOp():
    def __init__(self):
        self.n=[]
    def add(self,ele):
        return self.n.append(ele)
    def remove(self,item):
        return self.n.remove(item)
    def dis(self):
        return (self.n)

obj = listOp()
choice = 1
while choice != 0:
    print("0. Exit")
    print("1. Add")
    print("2. Remove")
    print("3. Display")

    choice = int(input("Enter choice: "))

    if choice == 1:
        n = int(input("Enter number to append: "))
        obj.add(n)

    elif choice == 2:
        n = int(input("Enter number to remove: "))
        obj.remove(n)

    elif choice == 3:
        print("List: ",obj.dis())
    
    elif choice == 0:
        print("Exiting")
        break
    
    else:
        print("invalid input choice!")