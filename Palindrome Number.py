class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0:
            return True
        temp = x
        original=0
        for i in range (len(str(x))): 
            if x!=0:
                original = original * 10 + x % 10
                x = x//10
               
            else: 
                return x

        if temp==original:
            return True 
        else:
            return False 
