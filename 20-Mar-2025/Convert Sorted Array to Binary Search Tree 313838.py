# Problem: Convert Sorted Array to Binary Search Tree - https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        nums.sort()
        n = len(nums)

        def build(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            middle = TreeNode(nums[mid])
            middle.left = build(left, mid - 1)
            middle.right = build(mid + 1, right)
            return middle

        return build(0, n - 1)               