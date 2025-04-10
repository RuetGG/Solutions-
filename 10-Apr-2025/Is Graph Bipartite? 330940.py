# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = {k: 2 for k in range(n)}
        no_cycle = True

        def dfs(node, curr):
            nonlocal no_cycle
            if not no_cycle:
                return 
            
            color[node] = curr
            for neighbor in graph[node]:
                if color[neighbor] == curr:
                    no_cycle = False
                    return   

                elif color[neighbor] == 2:
                    dfs(neighbor, -curr)

        for i in range(n):
            if color[i] == 2:
                dfs(i, 1)
            
        return no_cycle 