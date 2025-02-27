# Problem: D - Bomb Detection Validation - https://codeforces.com/gym/586960/problem/D

def inbound(i, j):
    return 0 <= i < n and 0 <= j < m

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
changes = {(0,1), (1,1), (1,0), (1,-1),(0,-1), (-1,-1),(-1,0), (-1,1)}

for r in range(n):
    for c in range(m):
        if board[r][c] == "*":
            continue
        
        count = 0
        for r_c, c_c in changes:
            i = r + r_c
            j = c + c_c
            if inbound(i, j) and board[i][j] == "*":
                count += 1
                
        if board[r][c] == "." and count != 0:
            print("NO")
            exit(0)
        elif board[r][c].isdigit() and count != int(board[r][c]):
            print("NO")
            exit(0)
print("YES")