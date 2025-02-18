# Problem: C - The Splitting Game - https://codeforces.com/gym/586960/problem/C

from collections import Counter
t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    right = Counter(s)
    left = Counter()
    maxi = 0
    
    for char in s:
        right[char] -= 1
        if right[char] == 0:
            del right[char]

        left[char] += 1
        maxi = max(maxi, len(right) + len(left))
    print(maxi)