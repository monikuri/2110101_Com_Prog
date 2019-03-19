file = open(input().strip())
students = []
for line in file:
    line = line.strip()
    # empty line
    if len(line) <= 0:
        continue
    student = line.split(';')
    # duplicated id
    if student[0] in [students[i][0] for i in range(len(students))]:
        continue
    score = float(student[3]) + float(student[4])
    grade = 'F'
    if 80 <= score <= 100: grade = 'A'
    elif 70 <= score < 80: grade = 'B'
    elif 60 <= score < 70: grade = 'C'
    elif 50 <= score < 60: grade = 'D'
    students.append([student[0], student[1] + ' ' + student[2], grade])
#print(students)
while True:
    id = input()
    if id == '-1':
        break
    found = False
    for student in students:
        #print(student[0],'==',id,'?')
        if student[0] == id:
            print(student)
            found = True
    if not found:
        print('Not Found')