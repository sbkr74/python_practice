# To find Remaining Days
days = int(input("Enter days: "))
temp = days%365
year = days/365
month = temp/30
remDays = temp%30

print("Year: {:.2f}".format(year))
print("Month:",round(month,2))
print("Remaining Days:",remDays)