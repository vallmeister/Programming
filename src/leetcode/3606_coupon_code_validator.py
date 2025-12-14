import re
from heapq import heappush, heappop
from typing import List


class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        n = len(code)
        pattern = r"[a-zA-Z0-9_]+"
        valid_lines = {"electronics", "grocery", "pharmacy", "restaurant"}
        heap = []
        for i in range(n):
            c = code[i]
            line = businessLine[i]
            if not re.fullmatch(pattern, c) or line not in valid_lines or not isActive[i]:
                continue
            heappush(heap, (line, c))
        ans = []
        while heap:
            _, c = heappop(heap)
            ans.append(c)
        return ans


s = Solution()
print(s.validateCoupons(["1OFw", "0MvB"], ["electronics", "pharmacy"], [True, True]))
