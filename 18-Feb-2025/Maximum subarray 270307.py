# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        maxi = nums[0]
        for i in range(1, len(nums)):
            maxi = max(maxi + nums[i], nums[i])
            res = max(res, maxi)
        return res 