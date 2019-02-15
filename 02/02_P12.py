a, b, c = [int(i) for i in input().split()]
if(a > b):
    a,b = b,a
if(b > c):
    b,c = c,b
if(a > c):
    a,c = c,a
if(a > b):
    a,b = b,a
if(b > c):
    b,c = c,b
if(a + b > c):
    print("YES")
else:
    print("NO")