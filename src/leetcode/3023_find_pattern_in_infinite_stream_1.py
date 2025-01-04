# Definition for an infinite stream.
from collections import deque
from typing import Optional, List


class InfiniteStream:
    def __init__(self, nums):
        self.numbers = iter(nums)

    def next(self) -> int:
        return next(self.numbers)


class Solution:
    def findPattern(self, stream: Optional['InfiniteStream'], pattern: List[int]) -> int:
        PRIME = 10 ** 9 + 7
        base = 3
        pattern_hash = 0
        for digit in pattern:
            pattern_hash = (pattern_hash * base + digit) % PRIME
        m = len(pattern)
        window = deque()
        window_hash = 0
        for start in range(10 ** 5 + m):
            digit = stream.next()
            window.append(digit)
            window_hash = (base * window_hash + digit) % PRIME
            if len(window) > m:
                window_hash = (window_hash - window.popleft() * base ** m) % PRIME
            if len(window) == m and pattern_hash == window_hash:
                if all(window[i] == pattern[i] for i in range(m)):
                    return start - m + 1
        return -1


s = Solution()
print(s.findPattern(InfiniteStream([1, 1, 1, 0, 1]), pattern=[0, 1]))
print(s.findPattern(InfiniteStream([0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0]),
                    [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0]))
