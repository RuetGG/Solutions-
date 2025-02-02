# Problem: Valid Palindrome - https://leetcode.com/problems/valid-palindrome/description/

import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = re.sub(r'[^A-Za-z0-9]', '', s)
        if s == s[::-1]:
            return True
        else:
            return False
        