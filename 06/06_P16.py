height_map = [int(e.strip()) for e in input().strip().split(',')]
count = 0
negative = False
for i in height_map:
    if i < 0:
        negative = True
    else:
        if negative:
            count += 1
        negative = False
print(count)