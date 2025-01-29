# Check leap year
year = int(input("Enter year: "))

if year%4==0:
    print(year,"is Leap year")
else:
    print(year,"is not Leap year.")


# Original way
if year%100==0:
    if year%400==0 and year%4==0:
        print(year,"is Leap year.")
    else:
        print(year,"is not Leap Year.")
else:
    print(year,"is not leap year")