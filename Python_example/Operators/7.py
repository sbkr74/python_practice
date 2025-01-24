# 7. Membership Operator

a = 10
b = 18

myList = [3,6,9,12,15,18]

if a in myList:
    print("answer1: True")
else:
    print("answer1: False")

if a not in myList:
    print("answer2: True")
else:
    print("answer2: False")

if b in myList:
    print("answer3: True")
else:
    print("answer3: False")


# Another Example
x = "Hello World"
y = {1:'a',2:'b'}

print("H in x:",('H' in x))                     # True
print("hello not in x:",('hello' not in x))     # True
print("1 in y:",(1 in y))                       # True
print("a in y:",('a' in y))                     # False