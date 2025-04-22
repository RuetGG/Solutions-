# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        visited = [[False for _ in range(n)]for _ in range(m)]
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        original_color = image[sr][sc]
    
        def inbound(r, c):
            return 0 <= r < m and 0 <= c < n

        def moves(r, c):
            image[r][c] = color
            visited[r][c] = True

            for rc, cc in directions:
                nr = r + rc
                nc = c + cc
                if inbound(nr, nc):
                    if not visited[nr][nc] and image[nr][nc] == original_color:
                        moves(nr, nc)


        if image[sr][sc] != color:
            moves(sr, sc)
        return image


