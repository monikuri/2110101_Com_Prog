import math
a,b,c = [int(i) for i in input().split()]
s = (a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print(area)