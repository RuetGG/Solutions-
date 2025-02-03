# Problem: Final Value of Variable After Performing Operations - https://leetcode.com/problems/final-value-of-variable-after-performing-operations

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans = 0
        for i in range(len(operations)):
            if operations[i] == "--X" or operations[i] == "X--":
                ans  -= 1
            else:
                ans += 1
        return ans