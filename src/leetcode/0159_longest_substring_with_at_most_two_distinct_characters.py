class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        chars = {}
        start = end = 0
        longest_substring = 0
        while end < len(s):
            if s[end] in chars:
                chars[s[end]] += 1
            else:
                chars[s[end]] = 1
            while len(chars.keys()) > 2:
                chars[s[start]] -= 1
                if chars[s[start]] == 0:
                    del chars[s[start]]
                start += 1
            longest_substring = max(longest_substring, end - start + 1)
            end += 1

        return longest_substring


sol = Solution()
print(sol.lengthOfLongestSubstringTwoDistinct('eceba'))
print(sol.lengthOfLongestSubstringTwoDistinct('ccaabbb'))
