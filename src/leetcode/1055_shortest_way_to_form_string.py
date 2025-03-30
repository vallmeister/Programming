class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        m = len(source)
        n = len(target)
        letters = set(source)
        i = j = 0
        ans = 0
        while j < n:
            if i == 0:
                ans += 1
            if target[j] not in letters:
                return -1
            elif source[i] == target[j]:
                i += 1
                j += 1
            else:
                i += 1
            i %= m
        return ans


s = Solution()
print(s.shortestWay(source="abc", target="abcbc"))
print(s.shortestWay(source="abc", target="acdbc"))
print(s.shortestWay(source="xyz", target="xzyxz"))
print(s.shortestWay(source="xyz", target="xzyxy"))
print(s.shortestWay(source="abc", target="abcb"))
