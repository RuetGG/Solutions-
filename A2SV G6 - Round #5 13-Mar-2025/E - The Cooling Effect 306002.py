# Problem: E - The Cooling Effect - https://codeforces.com/gym/591928/problem/E

q = int(input())
for _ in range(q):
    s = input()
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    t = list(map(int, input().split()))

    ans = [float('inf')] * (n)
    
    for i in range(k):
        ans[a[i] - 1] = t[i]
        
    forward = [float('inf')] * n
    forward[0] = ans[0]
    
    for i in range(1, n):
        forward[i] = min(forward[i - 1] + 1, ans[i])
        
    backward = [float('inf')] * n
    backward[-1] = ans[-1]
    
    for i in range(n - 2, -1, -1):
        backward[i] = min(backward[i + 1] + 1, ans[i])
        
    res = [min(forward[i], backward[i]) for i in range(n)]
    print(*res)