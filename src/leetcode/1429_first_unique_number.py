from collections import Counter, deque
from typing import List


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.count = Counter(nums)
        self.unique = deque(nums)

    def showFirstUnique(self) -> int:
        while self.unique and self.count[self.unique[0]] > 1:
            self.unique.popleft()
        if self.unique:
            return self.unique[0]
        return -1

    def add(self, value: int) -> None:
        self.count[value] += 1
        if self.count[value] == 1:
            self.unique.append(value)


f = FirstUnique([2, 3, 5])
print(f.unique)
