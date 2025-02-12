# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxi = 0
        l, r = 0, len(height) - 1
        while l < r:
            heights = min(height[l], height[r])
            width = r - l
            prod = heights * width
            maxi = max(maxi, prod)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxi