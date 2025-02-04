# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        my_dict = Counter(nums)
        res = []
        for key, value in my_dict.items():
            if value == 2:
                res.append(key)
        return res