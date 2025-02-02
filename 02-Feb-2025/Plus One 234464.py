# Problem: Plus One - https://leetcode.com/problems/plus-one/

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = int("".join(map(str,digits)))
        num += 1
        return [int(digit) for digit in str(num)]