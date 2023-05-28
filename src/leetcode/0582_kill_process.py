from collections import defaultdict, deque
from typing import List


class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        killed_processes = []
        n = len(pid)
        children = defaultdict(set)
        for i in range(n):
            process = pid[i]
            parent = ppid[i]
            children[parent].add(process)

        q = deque()
        q.append(kill)
        while q:
            node = q.popleft()
            killed_processes.append(node)
            for child in children[node]:
                q.append(child)
        return killed_processes


s = Solution()
print(s.killProcess([1, 3, 10, 5], ppid=[3, 0, 5, 3], kill=5))
print(s.killProcess([1], ppid=[0], kill=1))
