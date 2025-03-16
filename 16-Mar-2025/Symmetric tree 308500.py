# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        nodeR = root.right
        nodeL = root.left

        def check(nodeL, nodeR):
            if not nodeR and not nodeL:
                return True
            if not nodeL or not nodeR:
                return False
            
            if nodeL.val != nodeR.val:
                return False
                
            return check(nodeL.right, nodeR.left) and check(nodeL.left, nodeR.right)

        return check(nodeL, nodeR)
