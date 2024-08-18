from heapq import heappush, heappop


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = []
        heappush(heap, 1)
        seen = set()
        curr_ugly = 1

        for _ in range(n):
            curr_ugly = heappop(heap)
            for prime in [2, 3, 5]:
                next_ugly = curr_ugly * prime
                if next_ugly not in seen:
                    seen.add(next_ugly)
                    heappush(heap, next_ugly)
        return curr_ugly


s = Solution()
print(s.nthUglyNumber(10))
print(s.nthUglyNumber(1))
print(s.nthUglyNumber(11))
print(s.nthUglyNumber(100))
