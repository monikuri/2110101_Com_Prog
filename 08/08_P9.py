n = int(input())
majors = {}
for i in range(n):
    args = [e.strip() for e in input().strip().split(',')]
    for m in args[1:]:
        if m not in majors:
            majors[m] = []
        majors[m].append(args[0])
searches = [e.strip() for e in input().strip().split(',')]
for search in searches:
    print(search,'->',end=' ')
    if search in majors:
        applicants = majors[search]
        if len(applicants) > 0:
            print(', '.join(applicants))
        else:
            print('Not found')
    else:
        print('Not found')
