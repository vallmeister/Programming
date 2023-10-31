from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans = [pref[0]]
        for i in range(1, len(pref)):
            ans.append(pref[i-1] ^ pref[i])
        return ans


s = Solution()
print(s.findArray([5, 2, 0, 3, 1]))
print(s.findArray([13]))
