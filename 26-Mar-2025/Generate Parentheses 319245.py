# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        count = 0
        ans = []
        res = []
        
        def backtrack(count, ans, open):
            if len(ans) == n * 2:
                res.append(''.join(ans))
                return

            if open < n:
                ans.append("(")
                backtrack(count + 1, ans, open + 1)
                ans.pop()

            if count > 0:
                ans.append(")")
                backtrack(count - 1, ans, open)
                ans.pop()

        backtrack(0, ans, 0)
        return res
