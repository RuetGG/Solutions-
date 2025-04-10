# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)

        def dfs(node, visited):
            visited.add(node)
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    dfs(neighbor, visited)

        indegree = [0] * n
        for u, v in edges:
            indegree[v] += 1

        champ = [i for i in range(n) if indegree[i] == 0]
        if len(champ) != 1:
            return -1
        
        visited = set()
        dfs(champ[0], visited)

        return champ[0] if len(visited) == n else -1 