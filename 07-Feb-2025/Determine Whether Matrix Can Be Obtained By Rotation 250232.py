# Problem: Determine Whether Matrix Can Be Obtained By Rotation - https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        k = 4
        while k > 0:
            res = []
            for i in range(len(mat[0])):
                ans = []
                for j in range(len(mat)):
                    ans.append(mat[j][i])
                res.append(ans)

            temp = []
            for i in range(len(mat)):
                ans = []
                for j in range(len(mat[0]) - 1, -1, -1):
                    ans.append(res[i][j])
                temp.append(ans)
            mat = temp
            k -= 1
            if mat == target:
                return True
        return False

        