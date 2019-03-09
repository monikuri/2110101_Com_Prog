nums = []
n = int(input())
for i in range(n):
    nums.append(int(input()))
start, end = [int(e) for e in input().split()]
print(sum(nums[start:end+1]))