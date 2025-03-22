# Problem: Path Sum - https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def traverse(node, ans):
            if not node:
                return False
            ans += node.val
            if not node.left and not node.right:
                return ans == targetSum
            return traverse(node.left, ans) or traverse(node.right, ans)
           

        return traverse(root, 0)
        
            
            
                
        