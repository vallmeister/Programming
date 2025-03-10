class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        freq = [0] * 26
        left = ans = 0
        for right, letter in enumerate(s):
            freq[ord(letter) - ord('a')] += 1
            if right - left + 1 == k and all(freq[i] <= 1 for i in range(26)):
                ans += 1
            if right - left + 1 == k:
                freq[ord(s[left]) - ord('a')] -= 1
                left += 1
        return ans


sol = Solution()
print(sol.numKLenSubstrNoRepeats('havefunonleetcode', 5))
print(sol.numKLenSubstrNoRepeats('home', 5))
