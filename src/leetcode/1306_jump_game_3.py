from collections import deque


class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        q = deque()
        visited = set()
        q.append(start)
        while q:
            idx = q.popleft()
            if idx in visited:
                continue
            visited.add(idx)
            val = arr[idx]
            if val == 0:
                return True
            if idx - val >= 0:
                q.append(idx - val)
            if idx + val < len(arr):
                q.append(idx + val)
        return False

s = Solution()
print(s.canReach([4, 2, 3, 0, 3, 1, 2], 5))
print(s.canReach([4, 2, 3, 0, 3, 1, 2], 0))
print(s.canReach([3, 0, 2, 1, 2], 2))
