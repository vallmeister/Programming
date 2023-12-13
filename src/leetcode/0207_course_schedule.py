from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisite_list = [set() for _ in range(numCourses)]
        is_prerequisite_for = [set() for _ in range(numCourses)]
        for a, b in prerequisites:
            prerequisite_list[a].add(b)
            is_prerequisite_for[b].add(a)
        q = []
        for i in range(numCourses):
            if not prerequisite_list[i]:
                q.append(i)
        while q:
            numCourses -= len(q)
            next_q = []
            for course in q:
                for neighbor in is_prerequisite_for[course]:
                    prerequisite_list[neighbor].remove(course)
                    if not prerequisite_list[neighbor]:
                        next_q.append(neighbor)
            q = next_q
        return numCourses == 0


s = Solution()
print(s.canFinish(2, [[1, 0]]))
print(s.canFinish(2, [[1, 0], [0, 1]]))
