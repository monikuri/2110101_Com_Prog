students = {}
while True:
    args = input().strip().split()
    if int(args[0]) == -1:
        break
    students[args[0]] = set(args[1:])
c1, c2 = input().strip().split()
count = [0, 0, 0]
for std in students:
    courses = students[std]
    search = {c1, c2}
    intersect = len(courses & search)
    # both c1 and c2
    if intersect == 2:
        count[0] += 1
    # either c1 or c2
    if intersect == 1:
        count[1] += 1
    # c1 or c2 or both
    if intersect != 0:
        count[2] += 1
print(*count)