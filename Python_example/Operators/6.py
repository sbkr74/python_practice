# 6. Identity Operator

a = 10
b = 20

if a is b:
    print("answer1: same")
else:
    print("answer1: not same")

if id(a) == id(b):
    print("answer2: same")
else:
    print("answer2: not same")

a = 20

if a is b:
    print("answer3: same")
else:
    print("answer3: not same")

if a is not b:
    print("answer4: not same")
else:
    print("answer4: same")