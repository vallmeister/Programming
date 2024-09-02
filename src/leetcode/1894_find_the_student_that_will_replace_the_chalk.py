from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)
        ps = [0] * n
        ps[0] = chalk[0]
        for i in range(1, n):
            ps[i] = ps[i - 1] + chalk[i]
        k %= ps[-1]
        if k < chalk[0]:
            return 0
        left = 0
        right = n - 1
        student = -1
        while left <= right:
            mid = (left + right) // 2
            if k < ps[mid]:
                student = mid
                right = mid - 1
            else:
                left = mid + 1
        return student


s = Solution()
print(s.chalkReplacer([3, 4, 1, 2], k=25))
