from collections import deque

class MyStack:
    def __init__(self):
        self.Q = deque()

    def push(self, x: int) -> None:
        self.Q.append(x)
        for i in range(len(self.Q)-1):
            self.Q.append(self.Q.popleft())

    def pop(self) -> int:
        return self.Q.popleft()

    def top(self) -> int:
        return self.Q[0]
        
    def empty(self) -> bool:
        return len(self.Q)==0
