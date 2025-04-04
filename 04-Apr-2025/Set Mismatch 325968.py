# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        l = 0
        res = []
        nums.sort()

        while l < len(nums) - 1:
            if nums[l + 1] == nums[l]:
                res.append(nums[l])
            l += 1
        for i in range(1, len(nums) + 1):
            if i not in nums:
                res.append(i)
                break

        return res