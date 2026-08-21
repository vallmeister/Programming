class Solution:
    def minPenalty(self, period: int, lights: list[int], arrivalTime: list[int]) -> int:
        light = max(lights)
        ans = 0
        for t in arrivalTime:
            r = t % period
            if r < light:
                continue
            ans = max(ans, period - r)
        return ans
