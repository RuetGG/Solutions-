# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        m = len(grid)
        n = len(grid[0])
        visited = [[False for i in range(n)] for j in range(m)]

        def inbound(r, c):
            return 0 <= r < m and 0 <= c < n

        maxi = 0

        def findLand(area, row, col):
            nonlocal maxi 
            visited[row][col] = True
            for rc, cc in direction:
                nr = row + rc
                nc = col + cc
                if inbound(nr, nc) and grid[nr][nc]:
                    if not visited[nr][nc]:
                        area[0] += 1
                        findLand(area, nr, nc)

            maxi = max(maxi, area[0])

        
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    area = [1]
                    findLand(area, i, j)


        return maxi