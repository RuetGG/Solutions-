# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

t = int(input())
for _ in range (t):
    n = int(input())
    a = list(map(int, input().split()))
    l = 0
    ans = 0
    maxi = float('-inf')
    r = 0
    while r < n:
        if a[r] > 0:
            while l < n and a[l] > 0:
                maxi = max(maxi, a[l])
                l += 1
            ans += maxi
            maxi = float('-inf')
        
        else:
            while l < n and a[l] < 0 :
                maxi = max(maxi, a[l])
                l += 1
            ans += maxi
            maxi = float('-inf')
        r = l   
    print(ans)            