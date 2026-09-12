import math
from collections import defaultdict


class Solution:
    def validSubarrays(self, nums: list[int], k: int, queries: list[list[int]]) -> list[bool]:
        n = len(nums)
        block_size = int(math.sqrt(n))
        ans = [False] * len(queries)
        block_queries = []
        for i, (left, right) in enumerate(queries):
            block_queries.append((left // block_size, right, i))
        block_queries.sort()

        prev_block = -1
        distinct = odd = l = r = 0
        frequencies = defaultdict(int)
        for block, right, i in block_queries:
            left, _ = queries[i]
            if block != prev_block:
                prev_block = block
                distinct = 0
                frequencies = defaultdict(int)
                odd = 0
                l = r = left
            while r <= right:
                num = nums[r]
                if frequencies[num] == 0:
                    distinct += 1
                    odd += 1
                elif frequencies[num] % 2 == 0:
                    odd += 1
                elif frequencies[num] % 2 == 1:
                    odd -= 1
                frequencies[num] += 1
                r += 1

            while l < left:
                num = nums[l]
                if frequencies[num] % 2 == 0:
                    odd += 1
                elif frequencies[num] % 2 == 1:
                    odd -= 1
                if frequencies[num] == 1:
                    distinct -= 1
                frequencies[num] -= 1
                l += 1
            while l > left:
                l -= 1
                num = nums[l]
                if frequencies[num] == 0:
                    odd += 1
                    distinct += 1
                elif frequencies[num] % 2 == 1:
                    odd -= 1
                elif frequencies[num] % 2 == 0:
                    odd += 1
                frequencies[num] += 1
            ans[i] = distinct == k and odd == 0
        return ans


s = Solution()
print(s.validSubarrays(nums=[1, 2, 2, 1], k=2, queries=[[0, 1], [0, 3], [1, 2]]))
print(s.validSubarrays(nums=[3, 3, 3], k=1, queries=[[1, 2], [0, 2]]))
