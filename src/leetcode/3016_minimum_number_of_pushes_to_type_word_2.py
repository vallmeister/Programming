from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = Counter(word)
        ls = sorted((counter.values()), reverse=True)
        ans = 0
        for i, pushes in enumerate(ls):
            ans += (i // 8 + 1) * pushes
        return ans


s = Solution()
print(s.minimumPushes("aabbccddeeffgghhiiiiii"))
