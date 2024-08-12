from heapq import heappush, heappop
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        for num in nums:
            heappush(self.heap, num)
            while len(self.heap) > k:
                heappop(self.heap)
        self.k = k

    def add(self, val: int) -> int:
        heappush(self.heap, val)
        while len(self.heap) > self.k:
            heappop(self.heap)
        return self.heap[0]


kth_largest = KthLargest(3, [4, 5, 8, 2])
print(kth_largest.add(3))
print(kth_largest.add(5))
print(kth_largest.add(10))
print(kth_largest.add(9))
print(kth_largest.add(4))
