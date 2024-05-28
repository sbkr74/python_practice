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