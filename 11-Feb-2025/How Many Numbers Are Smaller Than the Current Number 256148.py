# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        order = {}
        count = 0
        ans = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] not in order:
                order[nums[i]] = [i]
            else:
                order[nums[i]].append(i)
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                count += 0
            else:
                count = i
            for i in order[sorted_nums[i]]:
                ans[i] = count
        return ans 