# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        r = len(nums) - 1
        i = r - 1
        while r > 0 and i >= 0:
            while i >= 0 and nums[i] < r - i:
                i -= 1
            r = i
            i -= 1
       
        if r == 0:
            return True
        else:
            return False