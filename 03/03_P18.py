import math
def is_prime(x):
    prime = True
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            prime = False
            break
    return prime
x = int(input())
if not is_prime(x):
    for i in range(2, x):
        if is_prime(i) and x % i == 0:
            print(i, end=' ')
