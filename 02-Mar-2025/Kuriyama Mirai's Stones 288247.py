# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

n = int(input())
v = list(map(int, input().split()))
curr_sum = 0
prefix1 = [0] * n

for i in range(n):
    curr_sum += v[i]
    prefix1[i] = curr_sum
    
v_sorted = sorted(v)
curr_sum = 0
prefix2 = [0] * n

for i in range(n):
     curr_sum += v_sorted[i]
     prefix2[i] = curr_sum
     
m = int(input())
for _ in range(m):
    type, l, r = map(int, input().split())
    l -= 1
    r -= 1
    
    if type == 1:
        if l > 0:
            ans = prefix1[r] - prefix1[l - 1]
        else:
            ans = prefix1[r]
    else:
        if l > 0:
            ans = prefix2[r] - prefix2[l - 1]
        else:
            ans = prefix2[r]
    print(ans)