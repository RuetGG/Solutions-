# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque([0])
        visited = set()

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                for neigh in rooms[node]:
                    if neigh not in visited:
                        queue.append(neigh)

        return len(visited) == len(rooms)