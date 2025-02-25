# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        stack = []
        maxi = float('-inf')
        while fast and fast.next:
            stack.append(slow.val)
            fast = fast.next.next
            slow = slow.next

        while slow:
            val1 = stack.pop()
            val2 = slow.val
            curr_sum = val1 + val2
            maxi = max(maxi, curr_sum)
            slow = slow.next
        return maxi