import math
a = float(input())
b = float(input())
C = math.radians(float(input()))
c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(C))
print("c =",c,"cm.")