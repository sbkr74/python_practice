# marksheet

rollno = int(input("Enter roll no: "))
phy = int(input("enter marks of physics: "))
che = int(input("enter marks of chemistry: "))
maths = int(input("enter marks of mathematics: "))
per = round((phy+che+maths)/3,2)
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
print(f'''-------------------
| Rollno: {rollno}     |
| Physics: {phy}     |
| Chemistry: {che}   |
| Maths: {maths}       |
| percentage: {per}|
| Grade: {grade}       |
-------------------
''')
