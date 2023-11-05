from typing import List


class Solution:
    PUSH = 'Push'
    POP = 'Pop'

    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        j = 0
        for i in range(1, n + 1):
            if j == len(target):
                break
            elif i == target[j]:
                ans.append(self.PUSH)
                j += 1
            else:
                ans.append(self.PUSH)
                ans.append(self.POP)
        return ans


s = Solution()
print(s.buildArray([1, 3], 3))
print(s.buildArray([1, 2, 3], 3))
print(s.buildArray([1, 2], 4))
