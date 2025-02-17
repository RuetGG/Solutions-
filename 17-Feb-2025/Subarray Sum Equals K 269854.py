# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_map = {0:1}
        acc = 0
        for num in nums:
            acc += num
            if acc - k in prefix_map:
                count += prefix_map[acc - k]
            if acc in prefix_map:
                prefix_map[acc] += 1
            else:
                prefix_map[acc] = 1
        return count         
        