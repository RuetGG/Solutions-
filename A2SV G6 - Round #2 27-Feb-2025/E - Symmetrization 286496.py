# Problem: E - Symmetrization - https://codeforces.com/gym/586960/problem/E

t = int(input())
for _ in range(t):
    n = int(input())
    a = [list(map(int, input().strip())) for _ in range(n)]
    count = 0
    for i in range((n + 1) // 2):
        for j in range(n // 2):
            x1, y1 = i, j
            x2, y2 = j, n - 1 - i
            x3, y3 = n - 1 - i, n - 1 - j
            x4, y4 = n - 1- j, i
            
            count0 = 0
            count1 = 0
            for x, y in [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]:
                if a[x][y] == 0:
                    count0 += 1
                else:
                    count1 += 1
            count += min(count0, count1)
    print(count)