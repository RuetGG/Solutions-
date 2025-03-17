# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []


        def level(nodes: List[TreeNode]):
            if not nodes:
                return

            maxi = float('-inf')
            nextR = []

            for node in nodes:
                if node:
                    maxi = max(maxi, node.val)
                if node.left:
                    nextR.append(node.left)
                if node.right:
                    nextR.append(node.right)
            ans.append(maxi)
            level(nextR)
 
        level([root])
        return ans

            
             
        