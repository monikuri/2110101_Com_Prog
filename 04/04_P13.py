s = input()
out = ""
k1 = input()
k2 = input()
for c in s:
    if c == k1:
        out += k2
    elif c == k2:
        out += k1
    else:
        out += c
print(out)