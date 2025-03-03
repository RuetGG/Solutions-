# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        ans = 0
        l = 1
        r = 2
        while r < len(nums):
            if nums[l] + nums[r] > nums[ans]:
                return nums[l] + nums[r] + nums[ans]
            l += 1
            r += 1
            ans += 1
        return 0
