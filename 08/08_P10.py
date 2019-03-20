n = int(input())
users = {}
ordered_users = []
for i in range(n):
    user, locations = input().strip().split(':')
    locations = [loc.strip() for loc in locations.strip().split(',')]
    users[user] = set(locations)
    ordered_users.append(user)
search = input().strip()
location = users[search]
found = False
for user in ordered_users:
    if len(users[user] & location) > 0 and user != search:
        print(user)
        found = True
if not found:
    print('Not Found')