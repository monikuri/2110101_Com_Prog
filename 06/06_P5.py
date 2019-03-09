nums = []
negative = 0
while True:
    x = int(input())
    if x < 0:
        negative = x
        break
    else:
        nums.append(x)
for x in nums:
    print(x + negative)