class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        while self.q1:
            self.q2.append(self.q1.pop(0))
        self.q1.append(x)
        while self.q2:
            self.q1.append(self.q2.pop(0))

    def pop(self) -> int:
        return self.q1.pop(0)

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        if not self.q1:
            return True
        return False
