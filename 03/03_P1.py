s = 0
while True:
    x = int(input())
    if x == -1:
        break
    if x%2 == 0:
        s += x
print(s)