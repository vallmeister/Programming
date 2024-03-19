from collections import Counter
from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        task_heap = [(-v, k) for k, v in counter.items()]
        heapify(task_heap)
        cooldown_heap = []
        t = 0
        while task_heap or cooldown_heap:
            while cooldown_heap and cooldown_heap[0][0] <= t:
                _, task = heappop(cooldown_heap)
                heappush(task_heap, (-counter[task], task))
            if task_heap:
                _, task = heappop(task_heap)
                counter[task] -= 1
                if counter[task] > 0:
                    heappush(cooldown_heap, (t + n + 1, task))
            t += 1

        return t


s = Solution()
print(s.leastInterval(["A", "A", "A", "B", "B", "B"], n=2))
print(s.leastInterval(["A", "C", "A", "B", "D", "B"], n=1))
print(s.leastInterval(["A", "A", "A", "B", "B", "B"], n=3))
