s = input()
start, end = [int(e) for e in input().split()]
if start - 0 > 0:
    print(s[0:start],end='')
print(s[start:end+1][::-1],end='')
if len(s) - 1 - end > 0:
    print(s[end+1:len(s)],end='')