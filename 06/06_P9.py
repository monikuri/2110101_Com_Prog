books = []
while True:
    cmd = input().split()
    if cmd[0] == 'end':
        break
    elif cmd[0] == 'return':
        books.append(' '.join(cmd[1:len(cmd)]))
        print(len(books))
    elif cmd[0] == 'list':
        print(books)
    elif cmd[0] == 'shelf':
        if len(books) > 0:
            print(books.pop())
        else:
            print('no book')
    elif cmd[0] == 'top':
        if len(books) > 0:
            print(books[len(books)-1])
        else:
            print('no book')