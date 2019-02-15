x = int(input())
not_prime = True
res = ""
for i in range(x-1,1,-1):
    if x%i == 0:
        print(i,end=' ')
        not_prime = False
if not_prime:
    print('Prime Number')