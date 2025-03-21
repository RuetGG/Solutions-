# Problem: Segment with Small Sum - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/A

n, s = map(int, input().split())
a = list(map(int, input().split()))
 
r = 0
max_len = 0
ans = 0
for l in range(n):
    ans += a[l]
    while ans > s:
        ans -= a[r]
        r += 1
    max_len = max(max_len, l - r + 1)
print(max_len)