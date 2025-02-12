# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count = [0] * (max(costs) + 1)
        for i in costs:
            count[i] += 1
        ans = 0
        for i in range(len(count)):
            while count[i] > 0 and coins >= i:
                coins -= i
                ans += 1
                count[i] -= 1 
        return ans