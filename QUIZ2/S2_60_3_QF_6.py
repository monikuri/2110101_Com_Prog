n = int(input())
applicants = {}
courses = {}
unassigned = []
admitted = {}
for i in range(n):
    args = input().strip().split()
    applicants[args[0]] = args[1:]
    unassigned.append(args[0])
m = int(input())
for i in range(m):
    args = input().strip().split()
    admitted[args[0]] = []
    courses[args[0]] = {
        'max': int(args[1]),
        'result': args[2:]
    }
while len(unassigned) > 0:
    ap = unassigned.pop()
    if len(applicants[ap]) > 0:
        c = applicants[ap].pop(0)
        admitted[c].append(ap)
        if len(admitted[c]) > courses[c]['max']:
            kicked = max([(courses[c]['result'].index(a),a) for a in admitted[c]])[1]
            admitted[c].pop(admitted[c].index(kicked))
            unassigned.append(kicked)
for c in sorted(admitted):
    print(c, *sorted(admitted[c]))