s = input()
replace = ['zero','one','two','three','four','five','six','seven','eight','nine']
out = ""
for i,c in enumerate(s):
    if c.isdigit():
        out += replace[int(c)]
        if i + 1 < len(s) and s[i+1].isalnum(): 
            out += ' '
    else:
        out += c
print(out)