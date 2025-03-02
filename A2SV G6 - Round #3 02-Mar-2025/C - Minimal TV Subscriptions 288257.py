# Problem: C - Minimal TV Subscriptions - https://codeforces.com/gym/588468/problem/C

from collections import Counter
t = int(input())
for _ in range(t):
    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))
    nums = Counter()
    for i in range (d):
        nums[a[i]] += 1
    min_sub = len(nums)

    for i in range(d, n):
        nums[a[i - d]] -= 1
        if nums[a[i - d]] == 0:
            del nums[a[i - d]]
        nums[a[i]] += 1
        min_sub = min(min_sub, len(nums))
    print(min_sub)