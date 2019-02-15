digits = [int(i) for i in list(input())]
s = 0
d = 13
for i in digits:
   s += i*d
   d -= 1
n13 = (11 - s%11)%10
print(n13)