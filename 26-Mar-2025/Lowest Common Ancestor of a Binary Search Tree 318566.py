# Problem: Lowest Common Ancestor of a Binary Search Tree - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        def search(node, p, q):
            if not node:
                return 

            curr = node.val
            if curr > p.val and curr > q.val:
                return search(node.left, p, q)
            elif curr < p.val and curr < q.val:
                return search(node.right, p, q)

            else:
                return node
                
            
        return search(root, p, q)              