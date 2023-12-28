import math
from functools import lru_cache


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)

        @lru_cache(None)
        def dp(idx, last_char, last_count, k):
            if k < 0:
                return math.inf
            elif idx == n:
                return 0

            delete_char = dp(idx + 1, last_char, last_count, k - 1)
            if s[idx] == last_char:
                keep_char = dp(idx + 1, last_char, last_count + 1, k) + (last_count in [1, 9, 99])
            else:
                keep_char = dp(idx + 1, s[idx], 1, k) + 1
            return min(delete_char, keep_char)

        return dp(0, '', 0, k)


sol = Solution()
print(sol.getLengthOfOptimalCompression("aaabcccd", k=2))
print(sol.getLengthOfOptimalCompression("aabbaa", k=2))
print(sol.getLengthOfOptimalCompression("aaaaaaaaaaa", k=0))
