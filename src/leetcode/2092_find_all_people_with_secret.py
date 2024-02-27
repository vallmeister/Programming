from collections import defaultdict, deque
from typing import List


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        accomplices = set()
        person_time = [[] for _ in range(n)]
        meetings.append([0, firstPerson, 0])
        meetings.sort(key=lambda e: e[2])
        adjacency_list = defaultdict(list)
        adjacency_list[(0, 0)].append((firstPerson, 0))
        for x, y, t in meetings:
            person_time[x].append(t)
            person_time[y].append(t)

            adjacency_list[(x, t)].append((y, t))
            adjacency_list[(y, t)].append((x, t))

        for person in range(n):
            if not person_time[person]:
                continue
            times = person_time[person]
            prev = times[0]
            for t in times[1:]:
                adjacency_list[(person, prev)].append((person, t))
                prev = t

        visited = set()
        q = deque()
        q.append((0, 0))
        while q:
            node, time = q.popleft()
            if (node, time) in visited:
                continue
            visited.add((node, time))
            accomplices.add(node)
            for neighbor in adjacency_list[(node, time)]:
                q.append(neighbor)

        return list(accomplices)


s = Solution()
print(s.findAllPeople(6, meetings=[[1, 2, 5], [2, 3, 8], [1, 5, 10]], firstPerson=1))
print(s.findAllPeople(4, meetings=[[3, 1, 3], [1, 2, 2], [0, 3, 3]], firstPerson=3))
print(s.findAllPeople(5, meetings=[[3, 4, 2], [1, 2, 1], [2, 3, 1]], firstPerson=1))
