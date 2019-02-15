s = input()
sum = sum([int(i) for i in s])
print(s,0 if sum%2 == 0 else 1,sep='')