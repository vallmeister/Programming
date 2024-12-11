from collections import Counter


class Solution:
    def maximumLength(self, s: str) -> int:
        s += '*'
        ans = -1
        counter = Counter()
        prev_char = s[0]
        streak = 1
        for c in s[1:]:
            if c == prev_char:
                streak += 1
                continue
            for i in reversed(range(1, streak + 1)):
                substring = prev_char * i
                counter[substring] += streak - i + 1
                if counter[substring] >= 3:
                    ans = max(ans, len(substring))
                    break
            prev_char = c
            streak = 1
        return ans


sol = Solution()
print(sol.maximumLength("abcccccdddd"))
