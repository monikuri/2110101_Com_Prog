s = input()
output = ""
for c in s:
    if c in ['"','\'',',','.','(',')']:
        output += ' '
    else:
        output += c
print(output)