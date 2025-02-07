# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transposed = []
        for i in range(len(matrix[0])):
            ans = []
            for j in range(len(matrix)):
                ans.append(matrix[j][i])
            transposed.append(ans)
        return transposed 