# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        for char in s:
            if char == "#":
                if not stack1:
                    pass
                else:
                    stack1.pop()
            else:
                stack1.append(char)
        for char in t:
            if char == "#":
                if not stack2:
                    pass
                else:
                    stack2.pop()
            else:
                stack2.append(char)
        return stack1 == stack2