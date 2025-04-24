# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        answer = [i for i in range(n)]
        indeg = defaultdict(int)
        adj_list = defaultdict(list)

        for u, v in richer:
            adj_list[u].append(v)
            indeg[v] += 1

        queue = deque(i for i in range(n) if indeg[i] == 0)
    
        while queue:
            node = queue.popleft()
            for neigh in adj_list[node]:
                if quiet[answer[node]] < quiet[answer[neigh]]:
                    answer[neigh] = answer[node]
                indeg[neigh] -= 1
                if indeg[neigh] == 0:
                    queue.append(neigh)

        return answer