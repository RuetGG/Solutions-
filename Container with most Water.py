class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        yaxis = 0
        maximum = 0
        while l < r:
            yaxis = min(height[l], height[r])
            xaxis = r - l
            result = yaxis * xaxis
            maximum = max(maximum, result)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return maximum
