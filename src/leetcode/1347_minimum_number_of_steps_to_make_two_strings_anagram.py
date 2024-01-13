from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counter_s = Counter(s)
        counter_t = Counter(t)
        for letter, count in counter_s.items():
            counter_t[letter] -= count
        return sum(abs(val) for val in counter_t.values()) // 2


print(Solution().minSteps("bab", t="aba"))
print(Solution().minSteps("leetcode", t="practice"))
print(Solution().minSteps("anagram", t="mangaar"))
