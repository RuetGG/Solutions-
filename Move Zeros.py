class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        left=0
        for x in range (len(nums)):
            if nums[x]:
                nums[left],nums[x]=nums[x],nums[left]
                left+=1

        return nums
