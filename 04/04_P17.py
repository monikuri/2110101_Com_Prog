s = input()
used = ""
out = ""
for c in s:
    if s.count(c) == 1:
        out += c
    else:
        if used.find(c) == -1:
            used += c
        else:
            if out.find(c) == -1:
                out += c
print(out)
