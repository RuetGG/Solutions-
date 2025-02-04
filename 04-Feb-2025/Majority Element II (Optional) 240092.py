# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        my_dict = Counter(nums)
        occurrence = len(nums) // 3
        res = [] 
        for num in my_dict:
            if my_dict[num] > occurrence:
                res.append(num)
        return res  