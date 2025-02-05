# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/description/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        m = 1
        if n == 1:
            return 1

        else:
            while time > 0:
                time -= 1
                m += 1
                if m == n:
                    while m > 1 and time > 0:
                        time -= 1
                        m -= 1                    
        return m