class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        chars = set()
        left = 0
        ans = 0
        for right, letter in enumerate(s):
            while letter in chars or right - left + 1 > k:
                chars.remove(s[left])
                left += 1
            chars.add(letter)
            if right - left + 1 == k:
                ans += 1
        return ans


sol = Solution()
print(sol.numKLenSubstrNoRepeats('havefunonleetcode', 5))
print(sol.numKLenSubstrNoRepeats('home', 5))
