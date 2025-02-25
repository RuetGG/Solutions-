# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        dummy = ListNode(0)
        prev = dummy
        add = 0
        while curr1 or curr2 or add:
            val1 = curr1.val if curr1 else 0
            val2 = curr2.val if curr2 else 0
            curr_sum = val1 + val2 + add

            add = curr_sum // 10
            nodeVal = curr_sum % 10  

            newNode = ListNode(nodeVal)
            prev.next = newNode
            prev = prev.next
            
            if curr1: curr1 = curr1.next
            if curr2: curr2 = curr2.next                          
        return dummy.next