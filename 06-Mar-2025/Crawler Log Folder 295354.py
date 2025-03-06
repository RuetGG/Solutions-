# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for dir in  logs:
            if dir != "./" and dir != "../":
                stack.append(dir)
            elif stack and dir == "../":
                stack.pop()
        count = 0
        while stack:
            count += 1
            stack.pop()
        return count 