n = int(input())
l = [i for i in range(1,n+1)]
while True:
    x, y = [int(e) for e in input().split()]
    if x == 0 and y == 0:
        break
    i = l.index(x)
    j = l.index(y)
    l[i], l[j] = l[j], l[i]
print(l)