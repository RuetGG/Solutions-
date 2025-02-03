# Problem: Roman to Integer - https://leetcode.com/problems/roman-to-integer/?envType=problem-list-v2&envId=string

class Solution:
    def romanToInt(self, s: str) -> int:
        my_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        i = 0
        ans = 0
        while i < len(s):
            if i+1 < len(s) and my_dict[s[i+1]] > my_dict[s[i]]:
                ans += my_dict[s[i+1]] - my_dict[s[i]]
                i += 2
            else:
                ans += my_dict[s[i]]
                i += 1
        return ans

            
        