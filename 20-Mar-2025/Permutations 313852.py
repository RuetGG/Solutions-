# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []

        def backtrack(ans):
            if len(ans) == len(nums):
                res.append(ans[:])
                return

            for i in range(len(nums)):
                if nums[i] in ans:
                    continue
                ans.append(nums[i])
                backtrack(ans)
                ans.pop()

        backtrack([])
        return res