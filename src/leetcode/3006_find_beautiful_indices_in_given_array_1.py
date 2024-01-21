from typing import List


class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        ans = []
        for i in range(len(s) - len(a) + 1):
            if s[i:].startswith(a):
                for j in range(max(0, i - k), min(len(s) - len(b) + 1, i + k + 1)):
                    if s[j:].startswith(b):
                        ans.append(i)
                        break
        return ans


print(Solution().beautifulIndices("wfvxfzut",  "wfv", "ut", 6))
