class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        n = len(s)
        window = [0] * 3
        right = n
        while right > 0 and any(count < k for count in window):
            right -= 1
            window[ord(s[right]) - ord('a')] += 1
        if any(count < k for count in window):
            return -1
        ans = n - right
        for left in range(n):
            window[ord(s[left]) - ord('a')] += 1
            while right < n and all(count >= k for count in window):
                ans = min(ans, left + 1 + n - right)
                window[ord(s[right]) - ord('a')] -= 1
                right += 1
            if all(count >= k for count in window):
                ans = min(ans, left + 1 + n - right)
        return ans


sol = Solution()
print(sol.takeCharacters("aabaaaacaabc", 2))
print(sol.takeCharacters('acba', 1))
print(sol.takeCharacters('aabbccca', 2))
