# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        arr = [0] * len(nums)
        i = 0
        l = k
        j = 0
        while j < l:
            arr[k - 1] = nums[len(nums) - j - 1]
            j += 1
            k -= 1
        while l < len(arr):
            arr[l] = nums[i]
            l += 1
            i += 1
        for i in range(len(arr)):
            nums[i] = arr[i]
