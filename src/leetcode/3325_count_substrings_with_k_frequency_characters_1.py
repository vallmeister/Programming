class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        appearances = [0] * 26
        ans = 0
        n = len(s)
        left = 0
        for right in range(n):
            appearances[ord(s[right]) - ord('a')] += 1
            while max(appearances) >= k:
                ans += n - right
                appearances[ord(s[left]) - ord('a')] -= 1
                left += 1
        return ans


sol = Solution()
print(sol.numberOfSubstrings('abacb', 2))
