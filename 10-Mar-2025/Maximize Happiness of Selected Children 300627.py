# Problem: Maximize Happiness of Selected Children - https://leetcode.com/problems/maximize-happiness-of-selected-children/?envType=daily-question&envId=2024-05-09

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        res = 0
        i  = len(happiness) - 1
        ans = 0
        while k > 0 and i >= 0:
            if (happiness[i] - ans)  >= 0:
                res += happiness[i] - ans 
            
            ans += 1
            k -= 1
            i -= 1
            
        return res