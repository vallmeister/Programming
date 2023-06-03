from collections import defaultdict
from heapq import heappush, nlargest
from typing import List


class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        student_scores = defaultdict(list)
        for item in items:
            sid, score = item
            heappush(student_scores[sid], score)
        res = []
        for sid in sorted(student_scores.keys()):
            res.append([sid, sum(nlargest(5, student_scores[sid])) // 5])
        return res


s = Solution()
print(s.highFive([[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]]))
print(s.highFive([[1, 100], [7, 100], [1, 100], [7, 100], [1, 100], [7, 100], [1, 100], [7, 100], [1, 100], [7, 100]]))
