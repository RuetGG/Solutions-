# Problem: Transformed Array - https://leetcode.com/problems/transformed-array/description/

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)  
        n = len(nums)
        
        for i in range(n):
            index = nums[i]
            if index > 0:
                ans[i] = nums[(i + index) % n] 
            else:
                ans[i] = nums[(i + index) % n]  
        
        return ans    