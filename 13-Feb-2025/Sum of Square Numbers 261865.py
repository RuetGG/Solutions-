# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c < 0:
            return False
  
        i = 0  
        square = []
        while i ** 2 <= c:
            square.append(i**2)
            i += 1
            
        left, right = 0, len(square) - 1
        curr_sum = 0
        while left <= right:
            curr_sum = square[left] + square[right]
            if curr_sum < c:
                left += 1
            elif curr_sum > c:
                right -= 1
            else:
                return True
        return False
        




        i = 1
        while res < c:

            res += square[i]
            i += 1
            if res == c:
                return True
        return False
        