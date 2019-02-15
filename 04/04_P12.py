s1 = input()
s2 = input()
pool = s1.replace(' ','').lower()
test = s2.replace(' ','').lower()
anagram = True
for c in test:
    if c in pool:
        pool = pool.replace(c,'',1)
    else:
        anagram = False
        break
anagram &= len(pool) <= 0
print(s1,s2 if not anagram else '')