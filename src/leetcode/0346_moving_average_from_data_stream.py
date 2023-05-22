from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.running_sum = 0
        self.buffer = deque()

    def next(self, val: int) -> float:
        self.buffer.append(val)
        self.running_sum += val
        while len(self.buffer) > self.size:
            self.running_sum -= self.buffer.popleft()
        return self.running_sum / len(self.buffer)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
