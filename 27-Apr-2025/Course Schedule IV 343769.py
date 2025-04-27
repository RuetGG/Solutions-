# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        reach = [set() for _ in range(numCourses)]
        answer = []

        for u, v in prerequisites:
            graph[u].append(v)

        for course in range(numCourses):
            queue = deque()
            visited = set()
            queue.append(course)

            while queue:
                node = queue.popleft()
    
                for neigh in graph[node]:
                    if neigh not in visited:
                        visited.add(neigh)
                        reach[course].add(neigh)
                        queue.append(neigh)
        answer = []
        for u, v in queries:
            answer.append(v in reach[u])

        return answer
