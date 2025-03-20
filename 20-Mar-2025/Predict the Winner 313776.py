# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        return self.fn(nums,0,len(nums) - 1) >= 0

    def fn(self,nums, left, right):
        if left == right:
            return nums[left]

        score_by_left = nums[left] - self.fn(nums, left + 1, right)
        score_by_right = nums[right] - self.fn(nums, left, right - 1)

        return max(score_by_left, score_by_right)