# Problem: I - The Odd Challenge - https://codeforces.com/gym/589822/problem/I

t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + a[i]
        
    total = prefix[n]
    
    for _ in range(q):
        l, r, k = map(int, input().split())
        l -= 1
        prev_sum = prefix[r] - prefix[l]
        curr_sum = (r - l) * k
        new_sum = total - prev_sum + curr_sum
        
        if new_sum % 2 != 0:
            print("YES")
        else:
            print("NO")