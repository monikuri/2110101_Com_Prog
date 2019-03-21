# post -- has liker --> {person1, person2, ...}
posts = {}
# person -- like --> {post1, post2, ...}
likes = {}
while True:
    args = input().strip().split()
    if args[0] == 'done':
        break
    liker = args[0]
    posters = args[1:]
    likes[liker] = set(posters)
    for poster in posters:
        if poster not in posts:
            posts[poster] = set()
        posts[poster].add(liker)
commands = input().strip().split()
cmd = commands[0]
if len(commands) > 1:
    args = commands[1:]
if cmd == 'R':
    for person in sorted(likes):
        print(person, len(likes[person]))
elif cmd == 'T':
    count_map = {}
    max_like = -1
    for poster in posts:
        count_like = len(posts[poster])
        max_like = max(max_like, count_like)
        if count_like not in count_map:
            count_map[count_like] = set()
        count_map[count_like].add(poster)
    for poster in sorted(count_map[max_like]):
        print(poster)
elif cmd == 'C':
    p1 = args[0]; p2 = args[1]
    p1_likes = posts[p1] if p1 in posts else set()
    p2_likes = posts[p2] if p2 in posts else set()
    common_likes = p1_likes & p2_likes
    if len(common_likes) > 0:
        for person in sorted(common_likes):
            print(person)
    else:
        print('None')
elif cmd == 'M':
    found = False
    for p1 in sorted(likes):
        if p1 in likes:
            for p2 in sorted(likes[p1]):
                if p2 in likes and p1 in likes[p2]:
                    print((p1, p2))
                    found = True
    if not found:
        print('None')