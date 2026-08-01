from typing import List


class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int],
                           waterDuration: List[int]) -> int:
        ans = 4000
        m = len(landDuration)
        n = len(waterDuration)
        for i in range(m):
            ls = landStartTime[i]
            ld = landDuration[i]
            for j in range(n):
                ws = waterStartTime[j]
                wd = waterDuration[j]
                if ls < ws:
                    ans = min(ans, max(ls + ld, ws) + wd)
                else:
                    ans = min(ans, max(ws + wd, ls) + ld)
        return ans


s = Solution()
print(s.earliestFinishTime(landStartTime=[2, 8], landDuration=[4, 1], waterStartTime=[6], waterDuration=[3]))
