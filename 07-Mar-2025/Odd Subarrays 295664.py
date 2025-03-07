# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    l = 0
    r = 1
    count = 0
    while r < n:
        if p[l] > p[r]:
            count += 1
            l += 2
            r += 2
        else:
            l += 1
            r += 1
    print(count)
    