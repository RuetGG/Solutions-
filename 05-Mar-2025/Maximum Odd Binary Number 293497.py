# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        nu = Counter(s)
        nu['1'] -= 1
        zeros = nu['0']
        ones = nu['1']
        arr = ['1'] * ones
        arr.append('0' * zeros)
        arr.append('1')
        return "".join(arr) 

       
        