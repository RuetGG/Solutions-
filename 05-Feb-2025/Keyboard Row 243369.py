# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        res = []
        for word in words:
            word1 = set(word.lower()) 
            if word1.issubset(row1) or word1.issubset(row2) or word1.issubset(row3):
                res.append(word)
        return res