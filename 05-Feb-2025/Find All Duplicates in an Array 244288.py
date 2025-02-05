# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        my_dict = Counter(nums)
        res = []
        for i, j in my_dict.items():
            if j == 2:
                res.append(i)
        return res