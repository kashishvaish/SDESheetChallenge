# Stack class.
class Stack:
    
    def __init__(self, capacity: int):
        # Write your code here.
        self.stack = []
        self.capacity = capacity

    def push(self, num: int) -> None:
        # Write your code here.
        if len(self.stack) < self.capacity:
            self.stack.append(num)

    def pop(self) -> int:
        # Write your code here.
        if not self.stack:
            return -1
        return self.stack.pop()
    
    def top(self) -> int:
        # Write your code here.
        if not self.stack:
            return -1
        return self.stack[-1]
    
    def isEmpty(self) -> int:
        # Write your code here.
        if not self.stack:
            return 1
        return 0
    
    def isFull(self) -> int:
        # Write your code here.
        if len(self.stack) == self.capacity:
            return 1
        return 0
