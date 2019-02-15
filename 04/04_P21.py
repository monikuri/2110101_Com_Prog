def match_all(str_list,index):
    c = str_list[0][index]
    for s in str_list:
        if s[index] != c:
            return False
    return True
n = int(input())
str_list = []
reversed_str_list = []
min_len = 999999999
for i in range(n):
    s = input()
    str_list.append(s)
    reversed_str_list.append(s[::-1])
    min_len = min(min_len,len(s))
# Search prefix
prefix_len = 0
for i in range(min_len):
    if match_all(str_list,i):
        prefix_len += 1
    else:
        break
print(str_list[0][0:prefix_len] if prefix_len > 0 else 'NO COMMON PREFIX')
# Search suffix
suffix_len = 0
for i in range(min_len):
    if match_all(reversed_str_list,i):
        suffix_len += 1
    else:
        break
print(reversed_str_list[0][0:suffix_len][::-1] if suffix_len > 0 else 'NO COMMON SUFFIX')