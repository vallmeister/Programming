class Solution:
    def compressedString(self, word: str) -> str:
        word += '*'
        prev = word[0]
        count = 1
        ans = []
        for c in word[1:]:
            if c != prev and count > 0:
                ans.append(str(count))
                ans.append(prev)
                prev = c
                count = 1
            else:
                count += 1
                prev = c
            if count == 9:
                ans.append(str(count))
                ans.append(prev)
                count = 0
        return ''.join(ans)
