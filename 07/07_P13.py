data = []
subject = None
found = False
while True:
    args = input().strip().split()
    if len(args) == 1:
        subject = -1*int(args[0])
        break
    else:
        data.append([float(args[1]), -1*int(args[0])])
data.sort(reverse=True)
for i, student in enumerate(data):
    if student[1] == subject:
        print(i+1)
        found = True
        break
if not found:
    print('Not Found')