table = []
first_row = [int(e) for e in input().strip().split()]
n = len(first_row)
r = (n + 1) // 2
table.append(first_row)
for i in range(r - 1):
    table.append([int(e) for e in input().strip().split()])
shift = 0
table_sum = 0
for i in reversed(range(r)):
    table_sum += sum(table[i][shift:n - shift])
    shift += 1
print(table_sum)