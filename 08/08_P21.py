nums = [int(e) for e in input().strip().split()]
num = int(input().strip())
count = 0
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == num:
            count += 1
print(count)