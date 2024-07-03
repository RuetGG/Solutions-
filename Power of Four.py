class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: float
        :rtype: bool
        """
        if not isinstance(n, int):
            return False
        if n==1:
            return True 
        if n%4 != 0:
            return False
        else:
            return self.isPowerOfFour(n/4)
