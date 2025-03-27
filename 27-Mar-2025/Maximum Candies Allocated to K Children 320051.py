# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if k > sum(candies):
            return 0

        def isPossible(mid):
            count = 0
            for c in candies:
                count += c // mid 
            if count >= k:
                return True
            else:
                return False
                    
        l = 1
        r = sum(candies) // k
        ans = 0

        while l <= r:
            mid = (l + r) // 2
            if isPossible(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans 

