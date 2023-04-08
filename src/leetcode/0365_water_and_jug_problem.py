from collections import deque


class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        q = deque()
        q.append((0, 0))
        visited = set()
        while q:
            j1, j2 = q.popleft()
            if j1 == targetCapacity or j2 == targetCapacity or j1 + j2 == targetCapacity:
                return True
            if (j1, j2) in visited:
                continue
            visited.add((j1, j2))

            # fill each jug
            q.append((jug1Capacity, j2))
            q.append((j1, jug2Capacity))

            # pour each jug
            q.append((0, j2))
            q.append((j1, 0))

            # pour j1 into j2
            left_capacity = jug2Capacity - j2
            if j1 <= left_capacity:
                q.append((0, j2 + j1))
            else:
                q.append((j1 - left_capacity, jug2Capacity))

            # pour j2 into j1
            left_capacity = jug1Capacity - j1
            if j2 <= left_capacity:
                q.append((j1 + j2, 0))
            else:
                q.append((jug1Capacity, j2 - left_capacity))
        return False


s = Solution()
print(s.canMeasureWater(3, 5, 4))
print(s.canMeasureWater(2, 6, 5))
print(s.canMeasureWater(1, 2, 3))
