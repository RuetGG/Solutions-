# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill5 = bill10 = bill20 = 0
        for bill in bills:
            if bill == 5:
                bill5 += 1
            elif bill == 10:
                if bill5 >= 1:
                    bill5 -= 1
                    bill10 += 1
                else:
                    return False
            elif bill == 20:
                if bill10 >= 1 and bill5 >= 1:
                    bill20 += 1
                    bill10 -= 1
                    bill5 -= 1
                elif bill5 >= 3:
                    bill20 += 1
                    bill5 -= 3
                else:
                    return False
        return True
