import math
T = input().strip()
B = tuple(T)
n = math.sqrt(len(B))
m = math.sqrt(n)
m = int(m); n = int(n)
if len(B) == m**4:
    for e in B:
        if not (1 <= (int(e) if e.isdigit() else -1) <= n):
            print('INPUT ERROR', e)
            exit(0)
    X = []
    for k in range(n):
        X += [B[k::n]]
    for k in range(n):
        S = set(X[k])
        if len(S) != n:
            print('C', k, 'ERROR', X[k])
            exit(0)
    for k in range(n):
        r = k//m*m; c = k%m*m
        S = set()
        for j in range(m):
            S.update(X[c+j][r:r+m])
        if len(S) != n:
            print('B', k, 'ERROR', X[c])
            exit(0)
    print('VALID', X[c])
    exit(0)
else:
    print('INCOMPLETE', T, m)
    exit(0)