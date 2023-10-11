import math
from bisect import bisect_left
from collections import defaultdict
from queue import PriorityQueue
from typing import List


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        n = len(people)
        answer = [-1] * n
        flowers.sort()
        full_bloom_at = defaultdict(PriorityQueue)
        # simple and stupid first
        for start, end in flowers:
            for key in {start for start, _ in flowers}:
                if start <= key <= end:
                    full_bloom_at[key].put(end)
        for idx, t in enumerate(people):
            if t in full_bloom_at:
                answer[idx] = len(full_bloom_at[t].queue)
            else:
                i = -1
                for key in full_bloom_at.keys():
                    if i < key < t:
                        i = key
                if i == -1:
                    answer[idx] = 0
                else:
                    l1 = sorted(full_bloom_at[i].queue)
                    k = bisect_left(l1, t)
                    tmp_q = PriorityQueue()
                    for num in l1[k:]:
                        tmp_q.put(num)
                    full_bloom_at[t] = tmp_q
                    answer[idx] = len(tmp_q.queue)
        return answer


s = Solution()
print(s.fullBloomFlowers([[1, 6], [3, 7], [9, 12], [4, 13]], people=[2, 3, 7, 11]))
print(s.fullBloomFlowers([[1, 10], [3, 3]], people=[3, 3, 2]))
print(s.fullBloomFlowers([[2, 6], [3, 7], [9, 12], [4, 13]], people=[1, 3, 7, 11]))
print(s.fullBloomFlowers([[19, 37], [19, 38], [19, 35]], [6, 7, 21, 1, 13, 37, 5, 37, 46, 43]))
print(s.fullBloomFlowers([[50, 50], [19, 27], [40, 46], [42, 48], [22, 46], [41, 50], [11, 36], [14, 29]],
                         [17, 35, 38]))  # 2, 2, 1
