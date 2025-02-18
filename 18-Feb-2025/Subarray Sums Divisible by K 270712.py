# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = 0
        count = 0
        pre = [0] * k
        pre[0] = 1
        for num in nums:
            prefix = (prefix + num) % k
            prefix = (prefix + k) % k
            count += pre[prefix]
            pre[prefix] += 1
        return count 