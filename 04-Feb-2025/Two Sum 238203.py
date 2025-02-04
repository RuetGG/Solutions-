# Problem: Two Sum - https://leetcode.com/problems/two-sum/description

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {} 
        for i, num in enumerate(nums):
            ans = target - num
            if ans in my_dict:
                return [my_dict[ans], i]
            my_dict[num] = i 
        return []    

        