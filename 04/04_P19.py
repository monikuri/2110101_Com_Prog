s = input()
k1 = input()
k2 = input()
out = ""
for c in s:
    found = False
    for i in range(len(k1)):
        if c == k1[i]:
            out += k2[i]
            found = True
            break
        elif c == k2[i]:
            out += k1[i]
            found = True
            break
    if not found:
        out += c
print(out)