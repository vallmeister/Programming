class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = 0
        indices = [[] for _ in range(26)]
        for i, char in enumerate(s):
            indices[ord(char) - ord('a')].append(i)
        for i in range(26):
            curr_indices = indices[i]
            if len(curr_indices) < 2:
                continue
            left = curr_indices[0]
            right = curr_indices[-1]
            for j in range(26):
                ans += self.binary_search(indices[j], left, right)
        return ans

    def binary_search(self, indices, lower, upper):
        left = 0
        right = len(indices) - 1
        while left <= right:
            mid = (left + right) // 2
            index = indices[mid]
            if index <= lower:
                left = mid + 1
            elif index >= upper:
                right = mid - 1
            else:
                return 1
        return 0


sol = Solution()
print(sol.countPalindromicSubsequence("aabca"))
print(sol.countPalindromicSubsequence("adc"))
print(sol.countPalindromicSubsequence("bbcbaba"))
