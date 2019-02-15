n = 0
total = 0
while True:
    x = float(input())
    if x < 0:
        break
    total += x
    n += 1
if n == 0:
    print('No data')
else:
    print(total/n)