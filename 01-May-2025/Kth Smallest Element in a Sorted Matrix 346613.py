# Problem: Kth Smallest Element in a Sorted Matrix - https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        index = 0
        p = []
        for i in  matrix :
            p.extend(i)
        heapq.heapify(p)

        for _ in range(k):
            
            if _ + 1 == k:
                return heapq.heappop(p)
            
            heapq.heappop(p)