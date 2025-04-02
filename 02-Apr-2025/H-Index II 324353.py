# Problem: H-Index II - https://leetcode.com/problems/h-index-ii/description/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l, r = 0, n - 1
        maxi = float('-inf')
        mini = float('inf')
        while l <= r:
            m = (l + r) // 2
            mini = min(citations[m], n - m)
            maxi = max(maxi, mini)
            
            if citations[m] < n - m:
                l = m + 1

            else:
                r = m - 1

        return maxi
            