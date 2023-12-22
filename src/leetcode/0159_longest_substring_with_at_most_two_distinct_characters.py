class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        ans = 0
        left = 0
        window = {}
        for right in range(len(s)):
            letter = s[right]
            if letter not in window:
                window[letter] = 0
            window[letter] += 1
            while len(window.keys()) > 2:
                letter = s[left]
                window[letter] -= 1
                left += 1
                if window[letter] == 0:
                    del window[letter]
            ans = max(ans, right - left + 1)
        return ans


sol = Solution()
print(sol.lengthOfLongestSubstringTwoDistinct('eceba'))
print(sol.lengthOfLongestSubstringTwoDistinct('ccaabbb'))
