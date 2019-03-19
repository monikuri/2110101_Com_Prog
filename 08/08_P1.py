n = int(input().strip())
union = set()
intersection = set()
for i in range(n):
    elements = set([int(e) for e in input().strip().split()])
    union = union.union(elements)
    if i == 0:
        intersection = elements
    else:
        intersection = intersection.intersection(elements)
print(len(union))
print(len(intersection))