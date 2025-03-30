from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = [-1] * 26
        offset = ord('a')
        for i, letter in enumerate(s):
            last_index[ord(letter) - offset] = i

        ans = []
        prev = curr = -1
        for i, letter in enumerate(s):
            curr = max(curr, last_index[ord(letter) - offset])
            if curr == i:
                ans.append(curr - prev)
                prev = curr
        return ans


sol = Solution()
print(sol.partitionLabels("ababcbacadefegdehijhklij"))
print(sol.partitionLabels("eccbbbbdec"))
