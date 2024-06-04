# Marksheet Example
name = input("Enter your Full Name: ")
rollNo = int(input("Enter Roll No: "))
phy = int(input("Enter score of Physics: "))
chem = int(input("Enter score of Chemistry: "))
maths = int(input("Enter score of Maths: "))
Total = phy + chem + maths
per = (Total/300)*100

print("Marsheet of student")
print("Full Name:",name)
print("Roll No:",rollNo)
print("Maths:",maths)
print("Physics:",phy)
print("Chemistry:",chem)
print("Total:",Total)
print("Percentage:",per)