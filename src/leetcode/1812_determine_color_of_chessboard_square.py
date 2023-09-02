class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        letter, digit = coordinates[0], int(coordinates[1])
        letter = ord(letter) - ord('a')
        digit -= 1
        return (letter + digit) % 2 == 1


s = Solution()
print(s.squareIsWhite('a1'))
print(s.squareIsWhite('h3'))
print(s.squareIsWhite('c7'))
