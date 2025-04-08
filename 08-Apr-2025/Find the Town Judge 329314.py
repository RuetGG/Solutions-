# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = [[] for _ in range(n + 1)]
        for u, v in trust:
            graph[u].append(v)

        index = -1
        for idx in range(1, n + 1):
            if len(graph[idx]) == 0:
                index = idx
                break

        if index != -1:
            for i in range(1, n + 1):
                if i != index and index not in graph[i]:
                    return -1
            return index
        
        return -1
        
