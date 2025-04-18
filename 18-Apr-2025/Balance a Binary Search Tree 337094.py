# Problem: Balance a Binary Search Tree - https://leetcode.com/problems/balance-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        vals = []

        def traverse(node):
            if node:
                traverse(node.left)
                vals.append(node.val)
                traverse(node.right)

        def build(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            return TreeNode(
                vals[mid],
                build(left, mid - 1),
                build(mid + 1, right)
            )

        traverse(root)
        return build(0, len(vals) - 1)

        