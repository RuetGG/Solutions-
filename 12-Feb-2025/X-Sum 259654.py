# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

t = int(input())

for _ in range(t):
    n, m = map(int, input().split()) 
    board = [list(map(int, input().split())) for _ in range(n)]  

    maxi = 0  
    for i in range(n):
        for j in range(m):
            temp = board[i][j]  
             
            # Traverse to top-left
            r, c = i - 1, j - 1
            while r >= 0 and c >= 0:
                temp += board[r][c]
                r -= 1
                c -= 1
            # Traverse to top-right
            r, c = i - 1, j + 1
            while r >= 0 and c < m:
                temp += board[r][c]
                r -= 1
                c += 1
            # Traverse to bottom-left
            r, c = i + 1, j - 1
            while r < n and c >= 0:
                temp += board[r][c]
                r += 1
                c -= 1
            # Traverse to bottom-right
            r, c = i + 1, j + 1
            while r < n and c < m:
                temp += board[r][c]
                r += 1
                c += 1
                
            maxi = max(maxi, temp)
    print(maxi)  