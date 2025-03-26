# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        def findDays(capacity):
            daysCount = 1
            curr = 0

            for weight in weights:
                if curr + weight > capacity:
                    daysCount += 1
                    curr = 0

                curr += weight

            return daysCount

        while l <= r:
            mid = (l + r) // 2 
            foundDays = findDays(mid)

            if foundDays <= days:
                r = mid - 1
            else:
                l = mid + 1 

        return l

        
        
