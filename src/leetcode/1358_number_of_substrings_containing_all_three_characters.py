class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        window = [0] * 3
        offset = ord('a')
        ans = left = 0
        for right in range(n):
            window[ord(s[right]) - offset] += 1
            while all(window):
                ans += n - right
                window[ord(s[left]) - offset] -= 1
                left += 1
        return ans


sol = Solution()
print(sol.numberOfSubstrings("abcabc"))
print(sol.numberOfSubstrings("aaacb"))
print(sol.numberOfSubstrings("abc"))
