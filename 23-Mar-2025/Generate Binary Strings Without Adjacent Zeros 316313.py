# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = []
        def backtrack(ans, count):
            if len(ans) == n:
                res.append(''.join(ans))
                return 

            ans.append('1')
            backtrack(ans, 0)
            ans.pop()

            if count < 1:
                ans.append('0')
                backtrack(ans, count + 1)
                ans.pop()

        backtrack([], 0)
        return res