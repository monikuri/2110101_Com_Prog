import numpy as np
n = int(input())
raw = []
for i in range(n):
    line = input().strip()
    if line[0] == '#' or 'STUDENT_ID' in line:
        continue
    raw.append([float(e) for e in line.split(',')[1:]])
res = np.array(raw)
print(*res.sum(axis=1),sep='\n')