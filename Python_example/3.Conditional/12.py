# nested-if another example (Hike negotation)

emp_id = int(input("Enter Employee ID: "))
yrs_of_exp = int(input("Years Of Exp: "))
sal = int(input("Salary: "))
dept = int(input("1.Tech\n2.Management\nChoose your Dept: "))
hike = 0
err = "Something went wrong.\nSelected Wrong option"
if dept == 1:
    sub_dept = int(input("1.AI\ML\n2.Data Engg\n3.IT\nChoose your Dept: "))
    if sub_dept == 1:
        inc = (sal*30)/100
        hike = sal+inc
    elif sub_dept == 2:
        inc = (sal*20)/100
        hike = sal+inc
    elif sub_dept == 3:
        inc = (sal*15)/100
        hike = sal+inc
    else:
        print(err)
    print(f"EmpNo:{emp_id}\tupdated Sal:${hike}")
elif dept == 2:
    sub_dept = int(input("1.Managers\n2.Sales\n3.Promoters\4.HR\nChoose your Dept: "))
    if sub_dept == 1:
        inc = (sal*30)/100
        hike = sal+inc
    elif sub_dept == 2:
        inc = (sal*20)/100
        hike = sal+inc
    elif sub_dept == 3:
        inc = (sal*25)/100
        hike = sal+inc
    elif sub_dept == 4:
        inc = (sal*10)/100
        hike = sal+inc
    else:
        print(err)
    print(f"{emp_id}:${hike}")
else:
    print(err)