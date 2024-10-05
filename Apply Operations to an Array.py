class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        length = len(nums)
        for x in range(length - 1):
            if nums[x] == nums[x+1]:
                nums[x] *= 2
                nums[x+1] = 0
        for x in range(length - 1, -1, -1):
            if nums[x] == 0:
                nums.pop(x)
                nums.append(0)
        return nums
