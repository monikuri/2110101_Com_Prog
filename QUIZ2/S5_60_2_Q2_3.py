n = int(input())
courses = {}
students = {}
registration = {}
# course -> faculty
for i in range(n):
    args = input().strip().split(',')
    if len(args) < 2:
        continue
    faculty = args[1]; course = args[0]
    courses[course] = faculty
m = int(input())
# course -> student
for i in range(m):
    course, student = input().strip().split(',')
    if student not in students:
        students[student] = set()
    students[student].add(course)
# search
query = set(input().strip().split(':'))
#  process data
for student in students:
    faculties = set()
    for course in students[student]:
        if course in courses:
            faculties.add(courses[course])
    count = len(query & faculties)
    if count not in registration:
        registration[count] = []
    registration[count].append(student)
# print
for reg in range(len(query),0,-1):
    if reg in registration:
        count = len(registration[reg])
    else:
        count = 0
    print('registered in',reg,'faculty:',count,'student')
    if reg in registration:
        for student in sorted(registration[reg]):
            print(student)