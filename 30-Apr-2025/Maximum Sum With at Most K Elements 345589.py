# Problem: Maximum Sum With at Most K Elements - https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/description/

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        for i in range(len(grid)):
            grid[i] = [-x for x in grid[i]]
            heapify(grid[i])

        tree = []
        for i in range(len(grid)):
            if grid[i]:
                heappush(tree, (grid[i][0], i))

        res = 0
        while k > 0 and tree:
            val, idx = heappop(tree)
            if limits[idx] == 0:
                continue

            res += -val
            limits[idx] -= 1
            k -= 1

            heappop(grid[idx])
            if grid[idx]:
                heappush(tree, (grid[idx][0], idx))

        return res