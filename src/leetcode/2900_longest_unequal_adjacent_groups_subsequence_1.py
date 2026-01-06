from typing import List


class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        dp = [0] * n
        index_of_next = [n] * n
        mx_val = mx_index = 0
        for i in reversed(range(n)):
            for j in range(i + 1, n):
                if groups[i] == groups[j]:
                    continue
                elif dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    index_of_next[i] = j
                if dp[i] > mx_val:
                    mx_val = dp[i]
                    mx_index = i
        ans = []
        while mx_index < n:
            ans.append(words[mx_index])
            mx_index = index_of_next[mx_index]
        return ans
