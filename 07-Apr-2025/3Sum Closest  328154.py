# Problem: 3Sum Closest  - https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if abs(total - target) < abs(closest_sum - target):
                    closest_sum = total
                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                else:
                    return total  
        return closest_sum
    