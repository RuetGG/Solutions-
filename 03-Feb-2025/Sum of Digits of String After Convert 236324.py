# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        for char in s:
            res = "".join((str(ord(char) - ord('a') + 1) for char in s))
        for _ in range(k):
            res = str(sum(int(digit) for digit in res))
            if len(res) == 1:
                break
        return int(res)