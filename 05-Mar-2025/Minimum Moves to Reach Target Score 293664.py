# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        while maxDoubles and target > 1:
            count += 1
            if target % 2 == 1:
                target -= 1
            else:
                maxDoubles -= 1
                target = target // 2
        count += target - 1
        return count 