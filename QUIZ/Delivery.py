# Input
date, month, year = [int(e) for e in input().split()]
delivery_type = input()
# find day in month
# apr, jun, sep, nov
day = 30
# jan, mar, may, jul, aug, oct, dec
if month in [1,3,5,7,8,10,12]:
    day = 31
# feb
elif month == 2:
    # christian era
    ce_year = year - 543
    if (ce_year%400 == 0) or (ce_year%4 == 0 and ce_year%100 != 0):
        day = 29
    else:
        day = 28
# Validate input
valid = True
if year < 2558:
    print('Invalid year')
    valid = False
elif month not in range(1,13):
    print('Invalid month')
    valid = False
elif date < 1 or date > day:
    print('Invalid date')
    valid = False
elif delivery_type not in ['E','Q','N','F']:
    print('Invalid delivery type')
    valid = False
# Process an input if valid
if valid:
    # Delivered on x/xx/xxxx
    delivery_date = ""
    # time taken to deliver in day(s)
    duration = 0
    if delivery_type == 'E':
        duration = 1
    elif delivery_type == 'Q':
        duration = 3
    elif delivery_type == 'N':
        duration = 7
    elif delivery_type == 'F':
        duration = 14
    # Calculate date
    shift_month = False
    if date + duration > day:
        delivery_date += str(duration - (day - date))
        shift_month = True
    else:
        delivery_date += str(date + duration)
    delivery_date += '/'
    # Calculate month
    shift_year = False
    if shift_month:
        if month + 1 > 12:
            delivery_date += '1'
            shift_year = True
        else:
            delivery_date += str(month + 1)
    else:
        delivery_date += str(month)
    delivery_date += '/'
    # Calculate year 
    if shift_year:
        delivery_date += str(year + 1)
    else:
        delivery_date += str(year)
    print('delivered on',delivery_date)