# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for idx, num in enumerate(temperatures):
            while stack and num > stack[-1][0]:
                val, index = stack.pop()
                ans[index] = idx - index
                
            stack.append((num,idx))
        return ans