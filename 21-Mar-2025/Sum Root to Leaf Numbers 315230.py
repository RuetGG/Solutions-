# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = []
        ans = []

        def traverse(node):
            if not node: 
                return

            ans.append(str(node.val))
            
            if not node.left and not node.right:
                num = int("".join(ans))
                res.append(num)

            else:
                if node.left:
                    traverse(node.left)
                if node.right:
                    traverse(node.right)
            ans.pop()


        traverse(root)
        fin = 0
        for num in res:
            fin += num
        return fin