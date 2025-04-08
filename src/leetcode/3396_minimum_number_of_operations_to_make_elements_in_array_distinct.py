from heapq import heappush, heappop
from typing import List


class Solution:
    # too complicated
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        freq = [0] * 101
        for num in nums:
            freq[num] += 1
        heap = []
        for i, f in enumerate(freq):
            if f == 0:
                continue
            heappush(heap, (-f, i))
        ans = i = 0
        while heap and heap[0][0] < -1:
            ans += 1
            for _ in range(3):
                if i >= n:
                    break
                freq[nums[i]] -= 1
                i += 1
            while heap and -heap[0][0] != freq[heap[0][1]]:
                _, num = heappop(heap)
                heappush(heap, (-freq[num], num))
        return ans


s = Solution()
print(s.minimumOperations([1, 2, 3, 4, 2, 3, 3, 5, 7]))
