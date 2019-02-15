op = input()
n = int(input())
str_list = []
invalid = False
# Input string list
for i in range(n):
    s = input().strip()
    if i > 0 and len(str_list[i-1]) != len(s):
        invalid = True
        break
    else:
        str_list.append(s)
# Invalid
if invalid:
    print('Invalid size')
elif op == '90':
    for i in range(len(str_list[0])):
        line = ''
        for j in reversed(range(n)):
            line += str_list[j][i]
        print(line)
elif op == 'flip':
    for s in str_list:
        print(s[::-1])
elif op == '180':
    for s in reversed(str_list):
        print(s[::-1])