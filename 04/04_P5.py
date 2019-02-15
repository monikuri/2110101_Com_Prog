s1, s2 = [e for e in input().split()]
sum = 0
for c in s2:
    sum += (int(c) if c.isdigit() else 0) 
print(s1.lower().title(),sum)