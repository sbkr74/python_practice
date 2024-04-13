# Program to swap Two numbers
a = 10
b = 20
print("Before swapping")
print("a:",a)
print("b:",b)
# ==============================================
#using 3rd variable
temp = a
a = b
b = temp

print("After swapping")
print("a:",a)
print("b:",b)
# ==============================================
# without using 3rd variable(arithmetic operator)
a = a+b
b = a-b
a = a-b

print("After swapping")
print("a:",a)
print("b:",b)
# ==============================================
# without using 3rd variable(bitwise operator)
a = a^b
b = a^b
a = a^b

print("After swapping")
print("a:",a)
print("b:",b)