l = input().strip().split()
order = [int(e) for e in input().strip().split()]
print(' '.join([l[i] for i in order]))