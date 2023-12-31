class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        last_seen = {}
        ans = -1
        for idx, char in enumerate(s):
            if char in last_seen:
                ans = max(ans, idx - last_seen[char] - 1)
            else:
                last_seen[char] = idx
        return ans


sol = Solution()
print(sol.maxLengthBetweenEqualCharacters('aa'))
print(sol.maxLengthBetweenEqualCharacters('abca'))
print(sol.maxLengthBetweenEqualCharacters('cbzxy'))
print(sol.maxLengthBetweenEqualCharacters("mgntdygtxrvxjnwksqhxuxtrv"))
