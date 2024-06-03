# Swap value
a = 10
b = 20

# using third variable
temp = a
a = b
b = temp
print("A:",a)
print("B:",b)

# using mathematical operator
a = a+b
b = a-b
a = a-b
print("A:",a)
print("B:",b)

# using operator
a = a^b
b = a^b
a = a^b
print("A:",a)
print("B:",b)