n = int(input())
data = {}
for i in range(n):
    key = int(input())
    if key not in data:
        data[key] = 0
    data[key] += 1
data_list = []
for key in data:
    data_list.append((data[key], -1*key))
data_list.sort(reverse=True)
print(-1*data_list[0][1])