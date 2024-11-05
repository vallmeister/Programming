from typing import List


class Solution:
    def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        char_ps = [[0] * 26 for _ in range(n + 1)]
        for i in range(1, n + 1):
            for char in range(26):
                char_ps[i][char] += char_ps[i - 1][char]
            char_ps[i][ord(s[i - 1]) - ord('a')] += 1
        ans = []
        for left, right in queries:
            count = 0
            for char in range(26):
                num = char_ps[right + 1][char] - char_ps[left][char]
                count += num * (num + 1) // 2
            ans.append(count)
        return ans


sol = Solution()
print(sol.sameEndSubstringCount("abcaab", [[0, 0], [1, 4], [2, 5], [0, 5]]))
