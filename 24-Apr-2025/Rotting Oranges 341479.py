# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        fresh = 0
        direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        def inbound(r, c):
            return 0 <= r < m and 0 <= c < n
        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh += 1

        minute = 0
        while queue:
            r, c, time = queue.popleft()
            minute = max(minute, time)

            for rc, cc in direction:
                nr = r + rc
                nc = c + cc
                if inbound(nr, nc) and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc, time + 1))

        return minute if fresh == 0 else -1