# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        n = len(isConnected)

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] and i != j:
                    adj_list[i].append(j)

        color = {i: 0 for i in range(n)}
        def dfs(node):
            if color[node] == 1:
                return

            color[node] = 1
            for neighbor in adj_list[node]:
                dfs(neighbor)

        count = 0
        for n in range(n):
            if color[n] == 0:
                count += 1 
                dfs(n)

        return count
        