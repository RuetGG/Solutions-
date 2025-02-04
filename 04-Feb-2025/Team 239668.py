# Problem: Team - https://codeforces.com/contest/231/problem/A

t = int(input())
ans = 0

for _ in range(t):
    n = list(map(int, input().split()))
    if n.count(1) > 1:
        ans += 1
print(ans)
    