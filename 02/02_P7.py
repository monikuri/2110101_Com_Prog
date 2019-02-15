month, year = [int(x) for x in input().split()]
year -= 543
if month == 2:
    if (year%4 == 0 and year%100 != 0) or year%400 == 0:
        print("29")
    else:
        print("28")
elif month in [1,3,5,7,8,10,12]:
    print("31")
else:
    print("30")