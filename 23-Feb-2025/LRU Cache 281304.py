# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

class Node:
    def __init__(self, key = 0, val = 0, next = None):
        self.key = key
        self.val = val
        self.next = next
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.head = Node()
        self.nodes = {} 
        self.tail = self.head

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1

        node = self.nodes[key]
        self.put(key, node.val)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            prev = self.head
            while prev.next and prev.next.key != key:
                prev = prev.next
            if prev.next:
                prev.next = prev.next.next
                if prev.next is None:
                    self.tail = prev
                
            node = self.nodes[key]
            
            if node == self.tail:
                node.val = value

       
        new_node = Node(key, value)
        self.tail.next = new_node
        self.tail = new_node

        self.nodes[key] = new_node

        if len(self.nodes) > self.capacity:
            least_used = self.head.next
            del self.nodes[least_used.key]
            self.head.next = least_used.next
            if self.head.next is None:
                self.tail = self.head
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)