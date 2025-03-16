# Problem: Binary Tree Preorder Traversal - https://leetcode.com/problems/binary-tree-preorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        lists=[]
        if not root:
             return lists
        def pre(node):
            if not node:
                return
            lists.append(node.val)
            pre(node.left) 
            pre(node.right)

        pre(root)
        return lists