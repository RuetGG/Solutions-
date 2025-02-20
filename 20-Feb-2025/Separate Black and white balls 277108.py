# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        if '0' not in s or '1' not in s:
            return 0
        l = 0 
        count = 0
        r = len(s) - 1
        while l < r:
            if s[l] == '1':
                while r > 1 and s[r] == '1':
                    r -= 1
                if l < r:
                    count += r - l
                    l += 1
                    r -= 1
            else:
                l += 1
        return count 