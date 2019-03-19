n = int(input())
students = []
groups = {}
nums = {}
majors = {}
for i in range(n):
    name, group, no, major = input().strip().split()
    students.append((name,group,no,major))
    if group not in groups:
        groups[group] = set()
    groups[group].add(i)
    if no not in nums:
        nums[no] = set()
    nums[no].add(i)
    if major not in majors:
        majors[major] = set()
    majors[major].add(i)
tags = input().strip().split()
result = set()
for tag in tags:
    if tag in groups:
        ids = groups[tag]
    elif tag in nums:
        ids = nums[tag]
    elif tag in majors:
        ids = majors[tag]
    else:
        ids = set()
    if len(result) == 0:
        result = ids
    else:
        result = result & ids
if len(result) == 0:
    print('Not Found')
else:
    for student in sorted([students[i] for i in result]):
        print(*student)