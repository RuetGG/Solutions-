# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        def flip(i, arr):
            l, r = 0, i
            while l < r:
                arr[l], arr[r] = arr[r], arr[l] 
                l += 1
                r -= 1

        for j in range(len(arr)):
            maxi = 0
            for i in range(len(arr) - j):
                if arr[maxi] < arr[i]:
                    maxi = i
            flip(maxi, arr)
            flip(len(arr) - j - 1, arr)
            ans.append(maxi + 1)
            ans.append(len(arr)- j)
        
        return ans 


                
