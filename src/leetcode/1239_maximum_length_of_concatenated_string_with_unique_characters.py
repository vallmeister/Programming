from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        arr = [substring for substring in arr if len(substring) == len(set(substring))]
        visited = [False] * 26
        ans = 0
        n = len(arr)

        def backtracking(idx, curr_len):
            nonlocal ans
            ans = max(ans, curr_len)
            if idx >= n:
                return
            for i in range(idx, n):
                substring = arr[i]
                if any(visited[ord(letter) - ord('a')] for letter in substring):
                    continue
                for letter in substring:
                    visited[ord(letter) - ord('a')] = True
                backtracking(i + 1, curr_len + len(substring))
                for letter in substring:
                    visited[ord(letter) - ord('a')] = False

        backtracking(0, 0)
        return ans


s = Solution()
print(s.maxLength(["un", "iq", "ue"]))
print(s.maxLength(["cha", "r", "act", "ers"]))
print(s.maxLength(["abcdefghijklmnopqrstuvwxyz"]))
print(s.maxLength(['aa', 'bb']))
