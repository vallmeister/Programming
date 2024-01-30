class Solution:
    def pivotInteger(self, n: int) -> int:
        ps = [0] * (n + 1)
        for i in range(1, n + 1):
            ps[i] = ps[i - 1] + i
        for i in range(1, n + 1):
            if ps[i] == ps[-1] - ps[i - 1]:
                return i
        return -1
