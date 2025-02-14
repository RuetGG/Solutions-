# Problem: Remove Duplicates from Sorted Array - https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 1
        n = len(nums)
        while r < len(nums):
            if nums[r] == nums[l]:
                nums.pop(r)
            else:
                r += 1
                l += 1
        diff = n - len(nums)
        nums.extend(['_'] * diff)
        return len(nums) - diff