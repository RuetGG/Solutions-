# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        res = 0
        emp = {e.id: e for e in employees}

        def traverse(node):
            nonlocal res
            if not node:
                return

            res += node.importance
            for sub in node.subordinates:
                traverse(emp[sub])

        for node in employees:
            if node.id == id:
                traverse(node)

        return res
             