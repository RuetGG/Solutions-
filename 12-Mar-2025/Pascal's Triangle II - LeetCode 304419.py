# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        prev = self.getRow(rowIndex - 1)
        curr = [1]
        for i in range(1, rowIndex):
            curr.append(prev[i-1] + prev[i])
            
        curr.append(1)
        return curr
        