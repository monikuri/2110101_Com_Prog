n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
u = 1
out = ''
out += str(u) + ' '
for i in  range(n-1):
    v = l[u-1]
    out += str(v) + ' '
    u = v
print(out)