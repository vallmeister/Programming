class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        num_substrings = 0
        chars = [0] * 128
        start = 0
        end = k - 1
        for i in range(k - 1):
            chars[ord(s[i])] += 1
        while end < len(s):
            chars[ord(s[end])] += 1
            end += 1
            if len(list(filter(lambda x: x > 1, chars))) == 0:
                num_substrings += 1
            chars[ord(s[start])] -= 1
            start += 1
        return num_substrings


sol = Solution()
print(sol.numKLenSubstrNoRepeats('havefunonleetcode', 5))
print(sol.numKLenSubstrNoRepeats('home', 5))
