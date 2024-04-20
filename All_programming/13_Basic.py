# leap year program
year = int(input("Enter a year: "))
if year%400==0:
  print("%d is leap year." %year)
else:
  if year%100==0:
    print("%d is not leap year." %year)
  elif year%4==0:
    print("% is leap year." %year)
