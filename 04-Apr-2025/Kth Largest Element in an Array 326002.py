# Problem: Kth Largest Element in an Array - https://leetcode.com/problems/kth-largest-element-in-an-array/description/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        r = len(nums) - 1
        n = len(nums)
        while l <= r:
            m = (l + r) // 2
            print(nums[m])
            if n - m > k:
                l = m + 1
            elif n - m < k:
                r = m - 1
            elif n - m == k:
                return nums[m]
