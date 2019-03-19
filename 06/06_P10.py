file = open(input().strip())
students = []
for line in file:
    student = line.strip().split(';')
    score = float(student[3]) + float(student[4])
    grade = 'F'
    if 80 <= score <= 100: grade = 'A'
    elif 70 <= score < 80: grade = 'B'
    elif 60 <= score < 70: grade = 'C'
    elif 50 <= score < 60: grade = 'D'
    students.append([student[0], student[1] + ' ' + student[2], grade])
print(students)