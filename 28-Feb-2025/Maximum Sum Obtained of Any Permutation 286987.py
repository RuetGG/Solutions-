# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        ans = [0] * (len(nums) + 1)
        for x, y in requests:
            ans[x] += 1
            ans[y + 1] -= 1

        curr_sum = 0
        for i in range(len(ans)):
            curr_sum += ans[i]
            ans[i] = curr_sum

        ans.sort(reverse = True)
        nums.sort(reverse = True)

        res = 0
        for i in range(len(nums)):
            res += ans[i] * nums[i]
        return res % (10**9 + 7)
