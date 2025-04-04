# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        l = 0
        while l + 1 < len(nums):
            if nums[l] == nums[l + 1]:
                res.append(nums[l])
            l += 1
        return res