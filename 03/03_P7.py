import math
x = float(input())
k = 0
cos = 0
term = 1
while True:
    term = ((-1)**k)*(x**(2*k))/math.factorial(2*k)
    if abs(term) <= 1e-8:
        break
    cos += term
    k += 1
print(cos,k-1)