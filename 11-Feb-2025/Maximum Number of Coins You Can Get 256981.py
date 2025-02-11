# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        l, r = 0, len(piles) - 1
        res = 0
        while l < r:
            r -= 1
            res += piles[r]
            l += 1
            r -= 1
        return res 