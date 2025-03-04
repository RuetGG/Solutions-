# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        l = 0
        rs = ls = 0
        while l < len(s):
            if s[l] == "R":
                rs += 1
            else:
                ls += 1
            if rs == ls:
                count += 1
                
            l += 1
        return count