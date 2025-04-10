# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        maxi = 0
        adj_list = defaultdict(list)
        for idx, val in enumerate(manager):
            adj_list[val].append(idx)

        def dfs(node, time):
            nonlocal maxi 
            time += informTime[node]

            if not adj_list[node]:
                maxi = max(maxi, time)
                return

            for neighbor in adj_list[node]:
                dfs(neighbor, time)

        dfs(headID, 0)
        return maxi