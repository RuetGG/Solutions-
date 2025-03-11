# Problem: D - Meklit's Chat Screen - https://codeforces.com/gym/594077/problem/D

from collections import deque

n, k = map(int, input().split())
m = list(map(int, input().split()))

queue = deque()
i = 0
check = set()
while i < n :
    Alen = len(check)
    check.add(m[i])
    Blen = len(check)
    
    if Alen != Blen:
        queue.appendleft(m[i])
    
    if Blen > k:
        val = queue.pop()
        check.remove(val)
         
    i += 1
    
print(len(queue))
print(*queue)