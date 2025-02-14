from typing import List


class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)

        non_inc = [0] * n
        for i in range(1, n):
            if security[i] <= security[i - 1]:
                non_inc[i] = non_inc[i - 1] + 1

        non_dec = [0] * n
        for i in reversed(range(n - 1)):
            if security[i] <= security[i + 1]:
                non_dec[i] = non_dec[i + 1] + 1

        ans = []
        for i in range(n):
            if non_inc[i] >= time and non_dec[i] >= time:
                ans.append(i)
        return ans
