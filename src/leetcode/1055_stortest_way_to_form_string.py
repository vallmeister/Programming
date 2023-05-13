class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        chars = set(source)
        i = 0
        subsequences = 0
        while i < len(target):
            j = 0
            while j < len(source) and i < len(target):
                if target[i] not in chars:
                    return -1
                elif target[i] == source[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
            subsequences += 1
        return subsequences


s = Solution()
print(s.shortestWay('abc', 'abcbc'))
print(s.shortestWay('abc', 'acdbc'))
print(s.shortestWay('xyz', 'xzyxz'))
print(s.shortestWay("aaaaa", "aaaaaaaaaaaaa"))
