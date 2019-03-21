# Solution by Prof. Sukree
n, m = input().split()
d = [int(x) for x in input().strip().split()]
os = [int(x) for x in input().strip().split()]
k = {}
for i in range(len(d)-1):
    for j in range(i+1, len(d)):
        st = d[i]+d[j]
        if st in k:
            k[st][0] += 1
        else:
            k[st] = [1, i, j]
lr = []
for ans in os:
    A = 'NO'
    for i in range(len(d)):
        if ans-d[i] in k:
            r = k[ans-d[i]]
            a1, a2, a3 = r
            if (a2 == i or a3 == i):
                A = A
            else:
                A = 'YES'
    print(A)
