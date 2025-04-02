# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0 
        r = (len(matrix) * len(matrix[0])) - 1
        while l <= r:
            m = (l + r) // 2
            i = m // len(matrix[0])
            j = m - (len(matrix[0]) * i)
            
            if matrix[i][j] > target:
                r = m - 1
            elif matrix[i][j] == target:
                return True
            else:
                l = m + 1
            
        return False

