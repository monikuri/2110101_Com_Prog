n, x = [int(i) for i in input().split()]
count = 0
for i in range(n):
    if int(input()) == x:
        count += 1
print(count)