# make a calculator
# using user-defined function 
# add(a,b) -> sum(a+b)
# sub(a,b) -> diff(a-b)
# mult(a,b) -> prod(a*b)
# div(a,b) -> div(a//b)
def add(a,b):
    add = a+b
    return add
def sub(a,b):
    sub = a-b
    return sub
def mult(a,b):
    mult = a*b
    return mult
def div(a,b):
    div = a//b
    return div

if __name__ == '__main__':
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(add(a,b))