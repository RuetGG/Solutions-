# Problem: Count Nodes Equal to Average of Subtree - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans = 0
        res = 0
        def check(node, count, ans):
            nonlocal res 

            if not node:
                return 0, 0

            left_sum, left_count = check(node.left, count, ans)
            right_sum, right_count = check(node.right, count, ans)

            count = left_count + right_count + 1
            ans = left_sum + right_sum + node.val

            if (ans // count) == node.val:
                res += 1
                
            return ans, count

        check(root, 0, 0)
        return res