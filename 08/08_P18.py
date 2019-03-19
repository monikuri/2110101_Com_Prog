stations = {}
while True:
    args = input().strip().split()
    if len(args) == 1:
        current = args[0]
        break
    if args[0] not in stations:
        stations[args[0]] = set()
    stations[args[0]].add(args[1])
    if args[1] not in stations:
        stations[args[1]] = set()
    stations[args[1]].add(args[0])
visited = set()
queue = [(current,0)]
while len(queue) > 0:
    u = queue.pop(0)
    visited.add(u[0])
    if u[0] in stations:
        for v in stations[u[0]]:
            if (v not in visited) and (u[1] + 1 <= 2):
                queue.append((v, u[1] + 1))
for station in sorted(visited):
    print(station)