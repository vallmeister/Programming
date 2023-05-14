class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        chars = {}
        start = end = 0
        max_so_far = 0
        while end < len(s):
            if s[end] in chars:
                chars[s[end]] += 1
            else:
                chars[s[end]] = 1
            while len(chars.keys()) > k:
                chars[s[start]] -= 1
                if chars[s[start]] == 0:
                    del chars[s[start]]
                start += 1
            max_so_far = max(max_so_far, end - start + 1)
            end += 1
        return max_so_far


sol = Solution()
print(sol.lengthOfLongestSubstringKDistinct('eceba', 2))
print(sol.lengthOfLongestSubstringKDistinct('aa', 1))
