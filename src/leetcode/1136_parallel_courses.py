from typing import List


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        semesters = 0
        requirements = [0] * (n + 1)
        next_courses = [set() for _ in range(n + 1)]
        for prev, nxt in relations:
            requirements[nxt] += 1
            next_courses[prev].add(nxt)
        q = []
        for i in range(1, n + 1):
            if requirements[i] == 0:
                q.append(i)
        if len(q) == 0:
            return -1
        while q:
            next_q = []
            for course in q:
                for next_course in next_courses[course]:
                    requirements[next_course] -= 1
                    if requirements[next_course] == 0:
                        next_q.append(next_course)
            q = next_q
            semesters += 1

        return semesters if sum(requirements) == 0 else -1


s = Solution()
print(s.minimumSemesters(3, relations=[[1, 3], [2, 3]]))
print(s.minimumSemesters(3, [[1, 2], [2, 3], [3, 1]]))
