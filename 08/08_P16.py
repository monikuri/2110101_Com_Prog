depts = {}
student_depts = []
student_rankings = []
for i in range(int(input())):
    dept, quota = input().strip().split()
    quota = int(quota)
    depts[dept] = quota
for i in range(int(input())):
    args = input().strip().split()
    id = args[0]
    score = float(args[1])
    selections = args[2:]
    student_rankings.append((score, id, selections))
student_rankings.sort(reverse=True)
for student in student_rankings:
    selected = ''
    for dept in student[2]:
        if depts[dept] > 0:
            selected = dept
            depts[dept] -= 1
            break
    student_depts.append((student[1], selected))
student_depts.sort()
for student in student_depts:
    print(*student)