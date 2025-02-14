# Problem: Books - https://codeforces.com/contest/279/problem/B

n, t = map(int, input().split())
a = list(map(int, input().split()))
l = 0
ans = 0
max_len = 0
for r in range(n):
    ans += a[r]
    while t < ans and l < n:
        ans -= a[l]
        l += 1
    max_len = max(max_len, r - l + 1)
print(max_len)