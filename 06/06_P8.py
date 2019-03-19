queue = list(input().strip())
n = int(input())
for i in range(n):
    cmd = input().split()
    if cmd[0] == 'in':
        queue.insert(int(cmd[2]),cmd[1])
    elif cmd[0] == 'out':
        queue.pop(int(cmd[1]))
    elif cmd[0] == 'swap':
        i = int(cmd[1])
        j = int(cmd[2])
        queue[i], queue[j] = queue[j], queue[i]
    print(''.join(queue))