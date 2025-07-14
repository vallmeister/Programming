class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        ans = curr = 0
        for bit in reversed(s):
            msb = int(bit) * 2 ** ans
            if curr + msb > k:
                continue
            ans += 1
            curr += msb
        return ans

    def dynamic_programming(self, s, k):
        n = len(s)
        # Reduce to LIS
        pass


sol = Solution()
print(sol.longestSubsequence(s="1001010", k=5))
print(sol.longestSubsequence("00101001", k=1))

print(sol.dynamic_programming(s="1001010", k=5))
print(sol.dynamic_programming("00101001", k=1))
