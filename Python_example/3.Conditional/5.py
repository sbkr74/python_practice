# Check leap year
year = int(input("Enter year: "))

print("Basic Check")
if year%4==0:
    print(year,"is Leap year")
else:
    print(year,"is not Leap year.")


# Original way
print("\nComplete check")
if year%4==0:
    if year%400==0:
        print(year,"is Leap year.")
    elif year%100==0:
        print(year,"is not Leap year.")
    else:
        print(year,"is Leap Year.")
else:
    print(year,"is not leap year")