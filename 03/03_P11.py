n = int(input())
total = 0
if n == 0:
    print('No Data')
else:
    for i in range(n):
        total += float(input())
    total /= n
    print(total)