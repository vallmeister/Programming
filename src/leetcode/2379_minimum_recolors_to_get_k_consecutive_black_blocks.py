class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = ans = len(blocks)
        left = window = 0
        for i in range(k - 1):
            if blocks[i] == 'W':
                window += 1
        for right in range(k - 1, n):
            if blocks[right] == 'W':
                window += 1
            ans = min(ans, window)
            if blocks[left] == 'W':
                window -= 1
            left += 1
        return ans
