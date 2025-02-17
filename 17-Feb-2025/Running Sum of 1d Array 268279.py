# Problem: Running Sum of 1d Array - https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr = []
        curr_sum = 0
        for num in nums:
            curr_sum += num
            arr.append(curr_sum)
        return arr
        