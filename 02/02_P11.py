ca , a = [int(i) for i in input().split()]
cb , b = [int(i) for i in input().split()]
need = cb - b
if a < need:
    b += a
    a = 0
else:
    b += need
    a -= need
print(a,b)