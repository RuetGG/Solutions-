# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        def inbound(r, c):
            return 0 <= r < m and 0 <= c < n
        direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        queue = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = -1

        while queue:
            r, c = queue.popleft()
    
            for rc, cc in direction:
                nr = r + rc
                nc = c + cc
                if inbound(nr, nc) and mat[nr][nc] == -1:
                    mat[nr][nc] = mat[r][c] + 1
                    queue.append((nr, nc))

        return mat