from typing import List


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m = len(box)
        n = len(box[0])
        output = [['.'] * m for _ in range(n)]
        for i in range(m):
            pos = n - 1
            for j in reversed(range(n)):
                if box[i][j] == '*':
                    output[j][m - i - 1] = '*'
                    pos = j - 1
                elif box[i][j] == '#':
                    output[pos][m - i - 1] = '#'
                    pos -= 1
        return output


s = Solution()
print(s.rotateTheBox([["#", ".", "*", "."], ["#", "#", "*", "."]]))
