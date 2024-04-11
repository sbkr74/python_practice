# Calculate area of triangle
# area = sqrt(s*(s-a)(s-b)(s-c))
a = int(input("Enter value of a:"))
b = int(input("Enter value of b:"))
c = int(input("Enter value of c:"))

s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print(area)
print("Area of Triangle: %.2f" %area)