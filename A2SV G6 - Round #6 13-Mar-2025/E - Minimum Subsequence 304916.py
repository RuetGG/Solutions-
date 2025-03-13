# Problem: E - Minimum Subsequence - https://codeforces.com/gym/594077/problem/E

from collections import Counter


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    
    
    zero = []
    one = []
    ans = 0
    res = []
    
    for i in range(n):
        if s[i] == '0':
            if not one:
                ans += 1
                res.append(ans)
                zero.append(ans)
                
            else:
                val = one.pop()
                res.append(val)
                zero.append(val)
                
        else:
            if zero:
                val = zero.pop()
                res.append(val)
                one.append(val)
                
            else:
                ans += 1
                res.append(ans)
                one.append(ans)
                
                 
    print(ans)
    print(*res)