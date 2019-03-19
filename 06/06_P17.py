rocks = [int(e) for e in input().strip().split()]
p1, p2 = [0,0]
player = 1
while len(rocks) > 0:
    left = rocks[0]
    right = rocks[len(rocks)-1]
    score = 0
    if left > right:
        score = left
        rocks.pop(0)
    else:
        score = right
        rocks.pop(len(rocks)-1)
    if player == 1:
        p1 += score
        player = 2
    else:
        p2 += score
        player = 1
print(p1)
print(p2)
print(1 if p1 > p2 else (2 if p2 > p1 else 0))