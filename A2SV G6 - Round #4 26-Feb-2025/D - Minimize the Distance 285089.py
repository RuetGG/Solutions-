# Problem: D - Minimize the Distance - https://codeforces.com/gym/590053/problem/D

n = int(input())
x = list(map(int, input().split()))
x.sort()
l = 0
r = n - 1
while l < r:
    l += 1
    r -= 1
    
if l == r:
        print(x[l]) 
          
if l > r:
    print(x[r])