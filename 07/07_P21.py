circulations = []
today = input().strip()
with open('circulations.txt') as f:
    for line in f:
        line = line.strip().split()
        book = line[0]
        member = line[1]
        due = line[2]
        if due < today:
            circulations.append([due, member, book])
circulations.sort()
if len(circulations) == 0:
    print('Not Found')
else:
    for book in circulations:
        print(book[2], book[1], book[0])