import math
x = int(input())
ans = -1
for a in range(1,int(x/3)):
    for b in range(1,x-a):
        c = x - (a+b)
        if c**2 == a**2 + b**2:
            ans = max(ans,c)
print(ans)