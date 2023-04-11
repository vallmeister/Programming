# The knows API is already defined for you.
# return a bool, whether a knows b
matrix = [[1, 1, 0], [0, 1, 0], [1, 1, 1]]


def knows(a: int, b: int) -> bool:
    pass


class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0
        for i in range(1, n):
            if candidate == i:
                continue
            if knows(candidate, i):
                candidate = i
        for i in range(n):
            if i == candidate:
                continue
            if knows(candidate, i) or not knows(i, candidate):
                return -1
        return candidate


s = Solution()
print(s.findCelebrity(3))
