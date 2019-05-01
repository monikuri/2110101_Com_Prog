import numpy as np
n = int(input())
# 0 -> grader, 1 -> pc
sep = ['\t', ' '][1]
prices = []
sales = []
for i in range(n):
    prices.append([float(input().strip().split(sep)[1])])
for i in range(n):
    sales.append([float(e) for e in input().strip().split(sep)[1:]])
res = (np.array(sales)*np.array(prices)).sum(axis=0)
print(*res,sep='\n')