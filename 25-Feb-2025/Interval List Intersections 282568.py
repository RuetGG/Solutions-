# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        left = 0
        right = 0
        ans = []
        while left < len(firstList) and right < len(secondList):

            maxi = max(firstList[left][0], secondList[right][0])
            mini = min(firstList[left][1], secondList[right][1])

            if maxi <= firstList[left][1] and maxi <= secondList[right][1] and mini >= firstList[left][0] and mini >= secondList[right][0]:
                ans.append([maxi, mini])
                
            if firstList[left][1] < secondList[right][1]:
                left += 1
            else:
                right += 1
        return ans 
