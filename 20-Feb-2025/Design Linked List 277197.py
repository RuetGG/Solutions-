# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.dummy = Node() 
        self.tail = None
        self.count = 0
        
    def get(self, index: int) -> int:
        if index >= self.count:
            return -1
        current = 0
        currentNode = self.dummy.next
        while current < index:
            currentNode = currentNode.next
            current += 1
        return currentNode.val

    def addAtHead(self, val: int) -> None:
        head = self.dummy.next
        newNode = Node(val)
        self.dummy.next = newNode
        newNode.next = head   

        self.count += 1  

        if not self.tail:
            self.tail = newNode
    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        if not self.tail:
            self.dummy.next = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.count += 1
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.count:
            return
        if index == self.count:
            self.addAtTail(val)
        else:
            current = 0
            currentNode = self.dummy
            while current < index:
                currentNode = currentNode.next
                current += 1
            newNode = Node(val)
            newNode.next = currentNode.next
            currentNode.next = newNode
            self.count += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.count:
            return
        current = 0
        currentNode = self.dummy
        while current < index:
            currentNode = currentNode.next
            current += 1
        currentNode.next = currentNode.next.next

        if not currentNode.next:
            self.tail = currentNode
        self.count -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)