from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        m = len(s)
        n = len(spaces)
        ans = []
        i = 0
        j = 0
        for _ in range(m + n):
            if j < n and spaces[j] + j == len(ans):
                ans.append(' ')
                j += 1
            else:
                ans.append(s[i])
                i += 1
        return ''.join(ans)


sol = Solution()
print(sol.addSpaces("LeetcodeHelpsMeLearn", [8, 13, 15]))
