# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        def search(node, key):
            if not node:
                return node

            if node.val > key:
                node.left = search(node.left, key)
            elif node.val < key:
                node.right = search(node.right, key)
            elif node.val == key:
                node = delete(node)

            return node

        def delete(node):
            if not node.right and not node.left:
                return None
            elif not node.left:
                return node.right
            elif not node.right:
                return node.left

            def minValue(n):
                curr = n
                while curr.left:
                    curr = curr.left
                return curr

            temp = minValue(node.right)
            node.val = temp.val
            node.right = search(node.right, temp.val)
            return node

        root = search(root, key)
        return root

       