from collections import defaultdict, deque
from typing import List


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[
        bool]:
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[a].append(b)
        is_required_for = defaultdict(set)

        def dfs(course):
            if course in is_required_for:
                return is_required_for[course]
            for next_course in graph[course]:
                descendant_courses = dfs(next_course)
                is_required_for[course].add(next_course)
                is_required_for[course] |= descendant_courses
            return is_required_for[course]

        for i in range(numCourses):
            dfs(i)

        ans = []
        for u, v in queries:
            ans.append(v in is_required_for[u])
        return ans

    def floyd_warshall(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]):
        g = [[False] * numCourses for _ in range(numCourses)]
        for a, b in prerequisites:
            g[a][b] = True

        for intermediate in range(numCourses):
            for a in range(numCourses):
                for b in range(numCourses):
                    g[a][b] = g[a][b] or g[a][intermediate] and g[intermediate][b]

        ans = []
        for u, v in queries:
            ans.append(g[u][v])
        return ans

    def topological_sort(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]):
        g = defaultdict(list)
        in_degree = [0] * numCourses
        for a, b in prerequisites:
            g[a].append(b)
            in_degree[b] += 1

        course_prerequisites = defaultdict(set)
        q = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)

        while q:
            node = q.popleft()
            for neighbor in g[node]:
                course_prerequisites[neighbor].add(node)
                course_prerequisites[neighbor] |= course_prerequisites[node]
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)

        ans = []
        for u, v in queries:
            ans.append(u in course_prerequisites[v])
        return ans


s = Solution()
print(s.checkIfPrerequisite(2, [[1, 0]], [[0, 1], [1, 0]]))
print(s.checkIfPrerequisite(2, [], [[0, 1], [1, 0]]))
print(s.checkIfPrerequisite(3, prerequisites=[[1, 2], [1, 0], [2, 0]], queries=[[1, 0], [1, 2]]))
