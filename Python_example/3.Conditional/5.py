# Check leap year
year = int(input("Enter year: "))

# if year%400==0:
#     print(year,"is Leap Year.")
# if year%100==0:
#     print(year,"is not Leap year.")

if year%4==0:
    print(year,"is Leap year")
else:
    print(year,"is not Leap year.")