#solution of Quadratic Equation
#   D=b*b - 4*a*c
# sol1 = (-b + sqrt(d))/2*a
# sol2 = (-b - sqrt(d))/2*a

import cmath
a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))

d = (b**2)-4*a*c

sol1 = (-b + cmath.sqrt(d))/2*a
sol2 = (-b - cmath.sqrt(d))/2*a

print("solution are {0} and {1}".format(sol1,sol2))