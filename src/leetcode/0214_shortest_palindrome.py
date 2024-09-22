class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        m = 2 * n + 1
        new_s = s + '#' + s[::-1]

        # Knuth-Morris-Pratt
        prefix = [0] * m
        for i in range(1, m):
            curr_match = prefix[i - 1]
            while curr_match > 0 and new_s[i] != new_s[curr_match]:
                curr_match = prefix[curr_match - 1]
            if new_s[i] == new_s[curr_match]:
                curr_match += 1
            prefix[i] = curr_match
        longest = prefix[-1]
        extent = s[longest:]
        return extent[::-1] + s

    def rolling_hash(self, s):
        hash_base = 29  # smallest prime > 26
        mod_value = int(10e9)
        forward_hash = reverse_hash = 0
        end = -1
        power_value = 1
        for i, char in enumerate(s):
            forward_hash = (forward_hash * hash_base + ord(char) - ord('a') + 1) % mod_value
            reverse_hash = (reverse_hash + (ord(char) - ord('a') + 1) * power_value) % mod_value
            power_value = (power_value * hash_base) % mod_value

            if forward_hash == reverse_hash:
                end = i
        suffix = s[end + 1:]
        return suffix[::-1] + s


sol = Solution()
print(sol.rolling_hash('abcd'))
