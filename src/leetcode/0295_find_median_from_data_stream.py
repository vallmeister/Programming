from heapq import heappush, heappop


class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if not self.min_heap and not self.max_heap:
            heappush(self.max_heap, -num)
        elif len(self.min_heap) < len(self.max_heap):
            heappush(self.min_heap, num)
            if self.min_heap[0] < -self.max_heap[0]:
                m = heappop(self.max_heap)
                m *= -1
                n = heappop(self.min_heap)
                heappush(self.min_heap, m)
                heappush(self.max_heap, -n)
        elif len(self.min_heap) == len(self.max_heap):
            heappush(self.max_heap, -num)
            if -self.max_heap[0] > self.min_heap[0]:
                m = heappop(self.max_heap)
                m *= -1
                n = heappop(self.min_heap)
                heappush(self.min_heap, m)
                heappush(self.max_heap, -n)

    def findMedian(self) -> float:
        if (len(self.min_heap) + len(self.max_heap)) % 2 == 0:
            return (self.min_heap[0] - self.max_heap[0]) / 2
        else:
            return -self.max_heap[0]


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.findMedian())
obj.addNum(3)
print(obj.findMedian())
