import math


class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        tx, ty = target
        ans = -1
        min_distance = math.inf
        for i, (x, y, r) in enumerate(drones):
            distance = abs(x - tx) + abs(y - ty)
            if distance <= r and distance < min_distance:
                ans = i
                min_distance = distance
        return ans
