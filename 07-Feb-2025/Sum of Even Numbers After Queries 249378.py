# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        res = 0
        for j in range(len(nums)):
            if nums[j] % 2 == 0:
                res += nums[j]

        for val, i in queries:
            temp_sum = val + nums[i]
            if temp_sum % 2 == 0:
                if nums[i] % 2 ==0:
                    res += val
                else:
                    res += temp_sum
            else:
                if nums[i] % 2 == 0:
                    res -= nums[i]
            nums[i] += val  
            ans.append(res)
        return ans
        