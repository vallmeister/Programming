import math


class Solution:
    def kthCharacter(self, k: int) -> str:
        return self.k_th_character_helper(k - 1)

    def k_th_character_helper(self, k):
        if k == 0:
            return 'a'
        elif k == 1:
            return 'b'
        ln = int(math.log2(k))
        char = self.k_th_character_helper(k - 2 ** ln)
        return chr(((ord(char) - ord('a') + 1) % 26) + ord('a'))


s = Solution()
print(s.kthCharacter(5))
print(s.kthCharacter(10))
