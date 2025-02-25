# Problem: Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        stack = []
        dummy = ListNode(0)
        prev = dummy
        curr = head
        while curr:
            count = 0
            temp = curr
            while curr and count < k:
                stack.append(curr.val)
                curr = curr.next
                count += 1
            if count == k:
                while stack:
                    val = stack.pop()
                    prev.next = ListNode(val)
                    prev = prev.next
            else:
                prev.next = temp
        return dummy.next