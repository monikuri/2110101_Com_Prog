import math
isbn = [int(i) for i in list(input())]
check = 0
d = 10
for n in isbn:
   check += d*n
   print(n,sep='',end='')
   d -= 1
print(math.ceil(check/11)*11 - check)