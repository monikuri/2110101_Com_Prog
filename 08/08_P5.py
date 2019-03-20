n = int(input())
winner = set()
loser = set()
for i in range(n):
    win, lose = [e for e in input().split()]
    winner.add(win)
    loser.add(lose)
print(sorted(winner - loser))