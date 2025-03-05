# marksheet

rollno = int(input("Enter roll no: "))
phy = int(input("enter marks of physics: "))
che = int(input("enter marks of chemistry: "))
maths = int(input("enter marks of mathematics: "))
total = (phy+che+maths)
per = round(total/3,2)
grade = None

if per < 40:
    grade = "D"
elif per > 40 and per <60:
    grade = "C"
elif per > 60 and per <80:
    grade = "B"
elif per > 80 and per <100:
    grade = "A "
else:
    print("Recheck the marks as it cannot cross 100 in any of one subjects")

print("\nMarsheet")
print(f"Rollno: {rollno}")
print(f"Physics: {phy}")
print(f"Chemistry: {che}")
print(f"Maths: {maths}")
print(f"Total: {total}")
print(f"percentage: {per}")
print(f"Grade: {grade}")