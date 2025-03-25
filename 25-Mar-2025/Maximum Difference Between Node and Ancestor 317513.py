# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None

        maxi = float('-inf')
        mini = float('inf')
        maxiAns = float(-inf)

        def traverse(node, maxi, mini):

            if not node:
                return maxi - mini

            maxi = max(maxi, node.val)
            mini = min(mini, node.val) 

            left = traverse(node.left, maxi, mini)
            right = traverse(node.right, maxi, mini)

            return max(left, right)
        
        return traverse(root, root.val, root.val)
            

        

