"""
TODO: Improve time complexity (33/100)
"""
n, m = [int(e) for e in input().split()]
nums = [int(e) for e in input().split()]
num_set = set(nums)
queries = [int(e) for e in input().split()]
for query in queries:
    found = False
    for i  in range(n):
        for j in range(i+1,n):
            a = nums[i]
            b = nums[j]
            c = query - (a+b)
            print(a, b, c)
            if (c in num_set) and (a != b  and b != c and a != c):
                found = True
                break
        if found:
            break
    print('YES' if found else 'NO')