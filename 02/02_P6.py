year = int(input())
year -= 543
if (year%4 == 0 and year%100 != 0) or year%400 == 0:
    print("29")
else:
    print("28")