# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diffs = []
        for x, y in costs:
            diffs.append([y - x, x, y])

        diffs.sort()
        ans = 0
        for i in range(len(diffs)):
            if i < len(diffs) // 2:
                ans += diffs[i][2]
            else:
                ans += diffs[i][1]

        return ans 
