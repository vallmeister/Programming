class Solution:
    def maximumGap(self, skill: str, station: str) -> int:
        m = len(station)
        n = len(skill)

        left_most = [n] * n
        right_most = [-1] * n

        i = j = 0
        while i < n and j < m:
            if skill[i] == station[j]:
                left_most[i] = j
                i += 1
                j += 1
            else:
                j += 1

        i = n - 1
        j = m - 1
        while i >= 0 and j >= 0:
            if skill[i] == station[j]:
                right_most[i] = j
                i -= 1
                j -= 1
            else:
                j -= 1

        gap = 0
        for i in range(n - 1):
            gap = max(gap, right_most[i + 1] - left_most[i])
        return gap
