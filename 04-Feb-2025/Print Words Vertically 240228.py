# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split(" ")
        res = []
        max_len = max(len(word) for word in words)
        
        for i in range(max_len):
            ans = ""
            for word in words:
                if i < len(word):
                    ans += word[i]
                else:
                    ans += " "
            res.append(ans.rstrip())
        return res