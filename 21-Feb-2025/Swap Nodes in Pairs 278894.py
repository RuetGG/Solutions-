# Problem: Swap Nodes in Pairs - https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prev = head 
        curr = prev.next
        head = curr
        while True:
            temp = curr.next
            curr.next = prev
            if not temp or not temp.next:
                prev.next = temp
                break
            prev.next = temp.next
            prev = temp
            curr = prev.next
            
        return head
