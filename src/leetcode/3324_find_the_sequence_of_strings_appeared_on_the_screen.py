from typing import List


class Solution:
    def stringSequence(self, target: str) -> List[str]:
        curr = []
        ans = []
        for c in target:
            curr.append('a')
            while curr[-1] != c:
                ans.append(''.join(curr))
                curr[-1] = chr(ord(curr[-1]) + 1)
            ans.append(''.join(curr))
        return ans
