# Problem: B - Jo's Adventure - https://codeforces.com/gym/590053/problem/B

n, m = map(int, input().split())
a = list(map(int, input().split()))
res = [0] * (n - 1)
for i in range(n - 1):
    if a[i] > a[i + 1]:
        res[i] = a[i] - a[i + 1]
        
ans = [0] * (n - 1)
for i in range(n - 1):
    if a[i] < a[i + 1]:
        ans[i] = a[i + 1] - a[i]
        
prefix = [0] * n
for i in range(1, n):
    prefix[i] = prefix[i - 1] + res[i - 1]

suffix = [0] * n 
for i in range(1, n):
    suffix[i] = suffix[i - 1] + ans[i - 1] 
for _ in range(m):
    s, t = map(int, input().split())
    s -= 1
    t -= 1
    if s < t:
        print(prefix[t] - prefix[s])
    else:    
        print(suffix[s] - suffix[t])