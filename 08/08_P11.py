books = []
tags = {}
with open('books.txt') as f:
    id = 0
    for line in f:
        args = [e.strip() for e in line.strip().split(',')]
        book_name = args[0]
        book_tags = args[1:]
        books.append(book_name)
        for tag in book_tags:
            if tag not in tags:
                tags[tag] = set()
            tags[tag].add(id)
        id += 1
input_tags = [e.strip() for e in input().strip().split(',')]
book_ids = set()
for tag in input_tags:
    if len(book_ids) == 0:
        book_ids = tags[tag]
    else:
        book_ids = book_ids & tags[tag]
if len(book_ids) == 0:
    print('Not found')
else:
    for book_id in sorted(book_ids):
        print(books[book_id])