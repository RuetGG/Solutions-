# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def check(time):
            count = 0
            for r in ranks:
                count += int(sqrt(time / r))
            return count

        l, r = 1, ranks[0] * cars * cars
        res = -1
        while l <= r:
            m = (l + r) // 2
            repaired = check(m)
            if repaired >= cars:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res