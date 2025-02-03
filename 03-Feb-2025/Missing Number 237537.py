# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maxi = max(nums)
        nums.sort()
        for i in range(maxi):
            if i != nums[i]:
                return i

        return maxi + 1