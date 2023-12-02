from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        ans = 0
        n = len(citations)
        i = 0
        j = n - 1
        while i <= j:
            mid = (i + j) // 2
            if citations[mid] >= mid + 1:
                ans = max(ans, mid + 1)
                i = mid + 1
            else:
                ans = max(ans, citations[mid])
                j = mid - 1
        return ans


s = Solution()
print(s.hIndex([3, 0, 6, 1, 5]))
print(s.hIndex([1, 3, 1]))
print(s.hIndex([1]))
