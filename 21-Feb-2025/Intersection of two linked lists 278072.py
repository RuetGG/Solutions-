# Problem: Intersection of two linked lists - https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nextPointer = set()
        temp1 = headA
        temp2 = headB
        while temp1 or temp2:
            if temp1 == temp2:
                return temp1
            else:
                if temp1 in nextPointer:
                    return temp1
                if temp2 in nextPointer:
                    return temp2
                if temp1:
                    nextPointer.add(temp1)
                    temp1 = temp1.next
                if temp2:
                    nextPointer.add(temp2)
                    temp2 = temp2.next
        return None