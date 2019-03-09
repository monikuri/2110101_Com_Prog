row = int(input())
col = int(input())
data = []
for i in range(row):
    input_row = [int(e) for e in input().strip().split()]
    data.append(input_row)
finish = False
for i in range(row):
    for j in range(i+1,row):
        if data[i] == data[j]:
            print(i+1)
            print(*data[i])
            print(j+1)
            print(*data[j])
            finish = True
            break
    if finish:
        break