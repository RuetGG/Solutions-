# Problem: D - Life Across the Stars - https://codeforces.com/gym/591928/problem/D

from collections import defaultdict


n = int(input())
prefix = defaultdict(int)
max_len = 0
for _ in range(n):
    b, d = map(int, input().split())
    max_len = max(max_len, d)
    prefix[b] += 1
    prefix[d] -= 1
    
curr_sum = 0
max_val = 0
idx = 0
for j in sorted(prefix.keys()): 
    curr_sum += prefix[j]
    if curr_sum > max_val:
        max_val = curr_sum
        idx = j
        
print(idx, max_val)