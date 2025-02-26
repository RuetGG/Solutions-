# Problem: B - Special Matrix Quest - https://codeforces.com/gym/586960/problem/B

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
res = 0
for i in range(n):
    # column
    res += board[i][(n - 1) // 2]
    # row
    res += board[(n - 1) // 2][i]
    # forward diagonal
    res += board[i][i]
    # backward diagonal
    res += board[i][n - i - 1]
res -= 3 * (board[(n - 1) // 2][(n - 1) // 2])
print(res)