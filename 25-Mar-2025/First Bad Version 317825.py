# Problem: First Bad Version - https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            mid = (l + r) // 2
            
            if not isBadVersion(mid):
                l = mid + 1
            else:
                if not isBadVersion(mid - 1):
                        return mid
                else:
                    r = mid - 1