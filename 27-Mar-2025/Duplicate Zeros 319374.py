# Problem: Duplicate Zeros - https://leetcode.com/problems/duplicate-zeros/description/?envType=problem-list-v2&envId=two-pointers

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        l = 0
        r = len(arr) - 1
        while l <= r:
            if arr[l] == 0:
                arr.insert(l + 1, 0)
                arr.pop()
                l += 1
            l += 1
        return arr
        