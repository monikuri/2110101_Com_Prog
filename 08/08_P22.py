nums = set([int(e) for e in input().strip().split()])
num = int(input())
count = 0
for i in nums:
    if (num - i) in nums:
        count += 1
print(count//2)