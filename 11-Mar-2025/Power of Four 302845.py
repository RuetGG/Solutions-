# Problem: Power of Four - https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        def check(prev, n):
            if prev > n:
                return False
            elif prev == n:
                return True
            return check(prev * 4, n) 

        prev = 1
        ans = check(prev, n)
        return ans 