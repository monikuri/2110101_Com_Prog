n = int(input())
freq = {'age': {}, 'province': {}}
for i in range(n):
    args = input().strip().split(',')
    age = int(args[1])
    province = args[3]
    if age not in freq['age']: freq['age'][age] = 0
    freq['age'][age] += 1
    if province not in freq['province']: freq['province'][province] = 0
    freq['province'][province] += 1
key, d1, d2 = input().strip().split(',')
result = []
if key == 'P':
    result = list(freq['province'].items())
elif key == 'A':
    result = list(freq['age'].items())
# https://docs.python.org/3/howto/sorting.html
result.sort(key=lambda x: x[0], reverse=(True if d2 == 'DSC' else False))
result.sort(key=lambda x: x[1], reverse=(True if d1 == 'DSC' else False))
for item in result:
    print(item[0], item[1])