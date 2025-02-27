# Problem: E - From S To T - https://codeforces.com/gym/585107/problem/E

from collections import Counter
test = int(input())

for _ in range(test):
    s = input()
    t = input()
    p = input()
    pCount = Counter(p)
    l = r = 0
    while r < len(t):
        if l < len(s) and s[l] == t[r]:
            l += 1
        elif t[r] in pCount and pCount[t[r]] > 0:
            pCount[t[r]] -= 1
        else:
            print("NO")
            break
        r += 1
    else:
        if l == len(s):
            print("YES")
        else:
            print("NO")