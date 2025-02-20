# Problem: Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode('0')
        prev = dummy
        curr = head
        while curr is not None:
            if prev.val == curr.val:
                prev.next = curr.next
                curr = curr.next
                continue
            prev = curr
            curr = curr.next
        return head