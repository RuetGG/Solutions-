# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def canPlaceBalls(min_dist):
            count, last_pos = 1, position[0]
            for pos in position[1:]:
                if pos - last_pos >= min_dist:
                    count += 1
                    last_pos = pos
                if count == m:
                    return True
            return False

        left, right = 1, position[-1] - position[0]
        result = 0

        while left <= right:
            mid = (left + right) // 2
            if canPlaceBalls(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result