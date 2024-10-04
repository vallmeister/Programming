class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = 'aeiou'
        n = len(word)
        ans = 0
        char_map = [[0] * 6 for _ in range(n + 1)]
        for i, char in enumerate(word):
            for j in range(6):
                char_map[i + 1][j] += char_map[i][j]
            if char in vowels:
                char_map[i + 1][vowels.index(char)] += 1
            else:
                char_map[i + 1][5] += 1
        for i in range(n):
            for j in range(1, n + 1):
                if all(char_map[j][k] > char_map[i][k] for k in range(5)) and char_map[j][5] - char_map[i][5] == k:
                    ans += 1
        return ans


s = Solution()
print(s.countOfSubstrings("aeiou", 0))
