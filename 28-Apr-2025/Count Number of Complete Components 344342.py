# Problem: Count Number of Complete Components - https://leetcode.com/problems/count-the-number-of-complete-components/

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        count = 0
        res = 0
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        queue = deque()

        def counter(queue, count):
            sub = set()
            nodes = set()
            while queue:
                node = queue.popleft()
                nodes.add(node)
                for nei in graph[node]:
                    sub.add((min(node, nei), max(node, nei)))
                    if nei not in visited:
                        queue.append(nei)
                        visited.add(nei)
            size = len(nodes)
            exp = size * (size - 1) // 2    
            return 1 if len(sub) == exp else 0
            
        for i in range(n):
            if i not in visited:
                print(i)
                queue.append(i)
                res += counter(queue, count)
        
        return res 