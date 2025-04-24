# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        indeg = defaultdict(int)
        n = len(graph)

        adj_list = defaultdict(list)
        for node in range(n):
            for nei in graph[node]:
                adj_list[nei].append(node)
                indeg[node] += 1

        queue = deque()
        for node in range(n):
            if indeg[node] == 0:
                queue.append(node)

        order = []
        while queue:
            node = queue.popleft()
            order.append(node)

            for nei in adj_list[node]:
                indeg[nei] -= 1

                if indeg[nei] == 0:
                    queue.append(nei)
        return sorted(order)

