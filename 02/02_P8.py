day = int(input())
month = int(input())
year = int(input())
year -= 543
for i in range(1,month):
    if i == 2:
        if (year%4 == 0 and year%100 != 0) or year%400 == 0:
            day += 29
        else:
            day += 28
    elif i in [1,3,5,7,8,10,12]:
        day += 31
    else:
        day += 30
print(day)