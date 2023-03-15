import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        num_queue = [1]
        res = []
        num_set = set(num_queue)
        heapq.heapify(num_queue)
        while len(res) < n:
            num = heapq.heappop(num_queue)
            if not num * 2 in num_set:
                num_set.add(num * 2)
                heapq.heappush(num_queue, num * 2)
            if not num * 3 in num_set:
                num_set.add(num * 3)
                heapq.heappush(num_queue, num * 3)
            if not num * 5 in num_set:
                num_set.add(num * 5)
                heapq.heappush(num_queue, num * 5)
            res.append(num)
        return res[n - 1]


s = Solution()
print(s.nthUglyNumber(10))
print(s.nthUglyNumber(1))
print(s.nthUglyNumber(11))
print(s.nthUglyNumber(100))
