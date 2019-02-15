def print_pair(i,j):
    print('('+str(i)+','+str(j)+')')
n, pattern = [int(i) for i in input().split()]
for i in range(n):
    if pattern == 1:
        for j in range(i,n):
            print_pair(i+1,j+1)
    elif pattern == 2:
        for j in range(0,i+1):
            print_pair(i+1,j+1)
    elif pattern == 3:
        print_pair(i+1,n-i)