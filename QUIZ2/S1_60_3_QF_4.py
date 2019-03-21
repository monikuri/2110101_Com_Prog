cards = input().strip().split()
commands = input().strip()
half = len(cards)//2
for cmd in commands:
    if cmd == 'C':
        left = cards[0:half]
        right = cards[half:]
        cards = right + left
    elif cmd == 'S':
        new_stack = []
        for i in range(half):
            new_stack += [cards[i], cards[i + half]]
        cards = new_stack
print(*cards)