class CustomStack:

    def __init__(self, maxSize: int):
        self.n = maxSize
        self.stack = [0] * maxSize
        self.size = 0

    def push(self, x: int) -> None:
        if self.size < self.n:
            self.stack[self.size] = x
            self.size += 1

    def pop(self) -> int:
        if self.size == 0:
            return -1
        self.size -= 1
        return self.stack[self.size]

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, self.size)):
            self.stack[i] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
