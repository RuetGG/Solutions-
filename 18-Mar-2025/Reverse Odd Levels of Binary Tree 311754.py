# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        self.level = 0

        def traverse(nodes: List[TreeNode]):
            self.level += 1
            if not nodes:
                return

            nextR = []
            for node in nodes:
                if node.left:
                    nextR.append(node.left)
                if node.right:
                    nextR.append(node.right)

            if self.level % 2 == 0:
                i, j = 0, len(nodes) - 1
                while i < j:
                    nodes[i].val, nodes[j].val = nodes[j].val, nodes[i].val
                    i += 1
                    j -= 1

            traverse(nextR)

        traverse([root])
        return root
