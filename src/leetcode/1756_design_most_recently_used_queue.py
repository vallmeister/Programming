class MRUQueue:

    def __init__(self, n: int):
        self.q = list(range(n + 1))

    def fetch(self, k: int) -> int:
        num = self.q.pop(k)
        self.q.append(num)
        return num

# obj = MRUQueue(n)
# param_1 = obj.fetch(k)