# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        left, right = 0 , 1
        point = 0
        popped = 0
        my_dict = Counter(nums)
        count = my_dict[0]
        while right < len(nums):
            if nums[left] == nums[right]:
                nums[left] *= 2
                nums.pop(right)
                popped += 1
            left += 1
            right += 1
            count += popped 
        while point < len(nums):
            if nums[point] == 0:
                nums.pop(point)
                popped += 1
                point -= 1
            point += 1
        nums.extend([0] * popped)
        return nums