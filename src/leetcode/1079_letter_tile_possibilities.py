class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        n = len(tiles)
        frequencies = [0] * 26
        for letter in tiles:
            frequencies[ord(letter) - ord('A')] += 1

        def backtrack(i):
            if i >= n:
                return 0
            ans = 0
            for j in range(26):
                if frequencies[j] == 0:
                    continue
                frequencies[j] -= 1
                ans += 1 + backtrack(i + 1)
                frequencies[j] += 1
            return ans

        return backtrack(0)


s = Solution()
print(s.numTilePossibilities('AAB'))
print(s.numTilePossibilities("AAABBC"))
