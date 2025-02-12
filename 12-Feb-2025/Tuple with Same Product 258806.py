# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        prod = {}
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                ans = nums[i] * nums[j]
                if ans not in prod:
                    prod[ans] = 1
                else:
                    prod[ans] += 1
        for i in prod.values():
            if i > 1:
                res += (i * (i - 1) // 2) * 8
        return res