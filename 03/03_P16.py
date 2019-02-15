import math
x = int(input())
sol = False
stop = False
for i in range(0,int(math.sqrt(x))):
    for j in range(0,x):
        if i**2 + j**2 == x:
            if i > j:
                stop = True
                break
            print(i,j)
            sol = True
        if stop:
            break
if not sol:
    print('No solution')