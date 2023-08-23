from collections import Counter
from heapq import heappop, heappush


class Solution:
    def reorganizeString(self, s: str) -> str:
        letters = Counter(s)
        q = []
        for k, v in letters.items():
            heappush(q, (-v, k))
        result = []
        n, c = heappop(q)
        result.append(c)
        if n < -1:
            heappush(q, (n + 1, c))
        while q:
            n, c = heappop(q)
            if c == result[-1]:
                if q:
                    n1, c1 = heappop(q)
                    result.append(c1)
                    if n1 < -1:
                        heappush(q, (n1 + 1, c1))
                    heappush(q, (n, c))
                else:
                    return ''
            else:
                result.append(c)
                if n < -1:
                    heappush(q, (n + 1, c))
        return ''.join(result)


sol = Solution()
print(sol.reorganizeString('aab'))
print(sol.reorganizeString('aaab'))
