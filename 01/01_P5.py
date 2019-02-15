import math
a = float(input())
b = float(input())
D = float(input())
C = math.radians(D)
area = (1/2)*a*b*math.sin(C)
print("area =",area,"(sq cm)")