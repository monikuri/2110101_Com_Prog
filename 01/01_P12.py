import math
a = float(input())
b = float(input())
c = float(input())
root = math.sqrt(b**2-4*a*c)
x1 = (-b+root)/(2*a)
x2 = (-b-root)/(2*a)
print("x1 = " + str(x1))
print("x2 = " + str(x2))