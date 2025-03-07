# Problem: Implement Queue using Stacks - https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if self.stack:
            return self.stack.popleft()
        return None
         
    def peek(self) -> int:
        if self.stack:
            return self.stack[0]
        return None

    def empty(self) -> bool:
        return not self.stack
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()