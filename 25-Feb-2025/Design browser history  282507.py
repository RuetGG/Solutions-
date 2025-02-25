# Problem: Design browser history  - https://leetcode.com/problems/design-browser-history/

class Node:
    def __init__(self, val = "", next = None, before = None):
        self.val = val
        self.next = next
        self.before = before

class BrowserHistory:

    def __init__(self, homepage: str):
        newNode = Node(homepage)
        self.prev = newNode
        self.curr = newNode

    def visit(self, url: str) -> None:
        newNode = Node(url)
        newNode.before = self.prev
        self.prev = newNode
        self.curr.next = self.prev
        self.curr = newNode 

    def back(self, steps: int) -> str:
        while self.curr.before and steps > 0:
            steps -= 1
            self.curr = self.curr.before
            self.prev = self.prev.before
        return self.curr.val


    def forward(self, steps: int) -> str:
        while self.curr.next and steps > 0:
            steps -= 1
            self.curr = self.curr.next
            self.prev = self.prev.next
        return self.curr.val
        
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)