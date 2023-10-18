from typing import List


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        prerequisites = [set() for _ in range(n + 1)]
        for source, target in relations:
            prerequisites[target].add(source)
        min_time = [0] * (n + 1)
        visited = set()

        def dfs(course):
            if course in visited:
                return min_time[course]
            visited.add(course)
            min_time[course] = time[course - 1]
            if prerequisites[course]:
                min_time[course] += max([dfs(pre) for pre in prerequisites[course]])
            return min_time[course]

        for i in range(1, n + 1):
            dfs(i)
        return max(min_time)


s = Solution()
print(s.minimumTime(3, [[1, 3], [2, 3]], time=[3, 2, 5]))
print(s.minimumTime(5, [[1, 5], [2, 5], [3, 5], [3, 4], [4, 5]], time=[1, 2, 3, 4, 5]))
print(s.minimumTime(9, [[2, 7], [2, 6], [3, 6], [4, 6], [7, 6], [2, 1], [3, 1], [4, 1], [6, 1], [7, 1],
                        [3, 8], [5, 8], [7, 8], [1, 9], [2, 9], [6, 9], [7, 9]], [9, 5, 9, 5, 8, 7, 7, 8, 4]))
