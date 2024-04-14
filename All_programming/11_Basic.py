# check number is +ve or -ve or 0.
num = int(input("Enter a number:"))
if num>0:
    print("%d is positive" %num)
else:
    if num==0:
        print("%d is zero" %num)
    else:
        print("%d is negative" %num)