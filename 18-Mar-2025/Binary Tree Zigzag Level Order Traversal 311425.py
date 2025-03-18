# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        self.level = 0
        res = []
        def traverse(nodes: List[TreeNode]):
            self.level += 1
            if not nodes:
                return 

            curr = []
            nextR = [] 
            for node in nodes:
                curr.append(node.val)
                if node.left:
                    nextR.append(node.left)
                if node.right:
                    nextR.append(node.right)
            if self.level % 2 == 0:
                curr.reverse()
                
            res.append(curr)
            traverse(nextR)
        
        traverse([root])
        return res
        




