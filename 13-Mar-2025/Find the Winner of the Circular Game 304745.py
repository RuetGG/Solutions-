# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        i = 0
        nums = [num for num in range(1, n + 1)]
        while len(nums) > 1:
            i = (i + k - 1) % len(nums)
            nums.pop(i)

        return nums[0] 