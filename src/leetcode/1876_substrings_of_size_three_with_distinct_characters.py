class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ans = 0
        window = []
        left = 0
        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left += 1
            window.append(s[right])
            while right - left + 1 > 3:
                window.remove(s[left])
                left += 1
            if right - left + 1 == 3 and len(window) == 3:
                ans += 1
        return ans


sol = Solution()
print(sol.countGoodSubstrings("xyzzaz"))
print(sol.countGoodSubstrings("aababcabc"))
print(sol.countGoodSubstrings("owuxoelszb"))
