# Problem: Possible Bipartition - https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for u, v in dislikes:
            adj_list[u].append(v)
            adj_list[v].append(u)

        color = {k: 0 for k in range(1, n + 1)}
        no_cycle = True

        def dfs(node, curr):
            nonlocal no_cycle
            if not no_cycle:
                return 
            color[node] = curr
            for neighbor in adj_list[node]:
                if color[neighbor] == 0:
                    dfs(neighbor, -curr)
                elif color[neighbor] == color[node]:
                    no_cycle = False
                    return

        for n in range(1, n + 1):
            if color[n] == 0:
                dfs(n, 1)

        return no_cycle
