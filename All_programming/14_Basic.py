# Largest among three digit
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
if(a>b) and (a>c):
  print("first number %d is the largest" %a)
elif b>c:
  print("second number %d is the largest" %b)
else:
  print("third number %d is the largest" %c)
