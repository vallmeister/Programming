class Solution:
    def toLowerCase(self, s: str) -> str:
        ans = []
        uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for letter in s:
            if letter in uppercase:
                ans.append(chr(ord(letter) + ord('a') - ord('A')))
            else:
                ans.append(letter)
        return ''.join(ans)
