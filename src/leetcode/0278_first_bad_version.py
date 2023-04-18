# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        while left <= n:
            mid = (left + n) // 2
            mid_version = isBadVersion(mid)
            if mid > 1 and mid_version and not isBadVersion(mid - 1):
                return mid
            elif mid_version:
                n = mid - 1
            elif not mid_version:
                left = mid + 1
        return 1
