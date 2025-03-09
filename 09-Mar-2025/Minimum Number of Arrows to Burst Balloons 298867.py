# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        count = 0
        last = float('-inf')
        sorted_point = sorted(points, key=lambda x:x[1])
        for x, y in sorted_point:
           if x > last:
            count += 1
            last = y
        return count
            

                                                                                                                                                                                                                                            