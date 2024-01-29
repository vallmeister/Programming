class MyQueue:

    def __init__(self):
        self.q = []
        self.helper = []

    def push(self, x: int) -> None:
        while self.q:
            self.helper.append(self.q.pop())
        self.q.append(x)
        while self.helper:
            self.q.append(self.helper.pop())

    def pop(self) -> int:
        return self.q.pop()

    def peek(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return not self.q

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()