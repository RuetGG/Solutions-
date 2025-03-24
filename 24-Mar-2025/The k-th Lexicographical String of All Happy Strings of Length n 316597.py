# Problem: The k-th Lexicographical String of All Happy Strings of Length n - https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/description/

class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        res = []
        ans = []
        def backtrack(countA, countB, countC, ans):

            if len(ans) == n:
                res.append(''.join(ans))
                return
             
            if countA < 1:
                ans.append("a")
                backtrack(1, 0, 0, ans)
                ans.pop()

            if countB < 1:
                ans.append("b")
                backtrack(0, 1, 0, ans)
                ans.pop()

            if countC < 1:
                ans.append("c")
                backtrack(0, 0, 1, ans)
                ans.pop()


        backtrack(0, 0, 0, [])
        print(res)

        return res[k - 1] if k - 1 < len(res) else ""

            