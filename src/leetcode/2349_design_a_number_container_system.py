from collections import defaultdict
from heapq import heappush, heappop


class NumberContainers:

    def __init__(self):
        self.number_at = defaultdict(int)
        self.first_index_of = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        self.number_at[index] = number
        heappush(self.first_index_of[number], index)

    def find(self, number: int) -> int:
        while self.first_index_of[number]:
            index = self.first_index_of[number][0]
            if self.number_at[index] == number:
                return index
            heappop(self.first_index_of[number])
        return -1
