# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        def inbound(r, c):
            return 0 <= r < m and 0 <= c < n
        direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        queue = deque()
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    isWater[i][j] = 0
                    queue.append((i, j))
                else:
                    isWater[i][j] = -1

        while queue:
            r, c = queue.popleft()
            for rc, cc in direction:
                nr = r + rc
                nc = c + cc
                if inbound(nr, nc) and isWater[nr][nc] == -1:
                    isWater[nr][nc] = isWater[r][c] + 1
                    queue.append((nr, nc))

        return isWater
