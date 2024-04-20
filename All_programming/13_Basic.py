# leap year program
year = int(input("Enter a year: "))
if year%4==0:
  if year%100=0:
    if year%400=0:
      print("%d is leap year" %year)
    else:
      print("%d is not leap year" %year)
  else:
    print("%d is leap year" %year)
else:
  print("%d is not leap year" %year)
