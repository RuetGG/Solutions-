# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        count = 0
        index = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
                index = i
            else:
                prod *= nums[i]
        res = [0] * len(nums)
        for i in range(len(nums)):
            if count == 0:
                res[i] = prod//nums[i] 
            else:
                if count == 1:
                    res[index] = prod
        return res