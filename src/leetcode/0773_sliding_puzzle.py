from collections import deque
from typing import List


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        target = "123450"
        q = deque()
        q.append((''.join([str(i) for i in board[0]]) + ''.join([str(i) for i in board[1]]), 0))
        visited = set()
        while q:
            state, dist = q.popleft()
            if state == target:
                return dist
            elif state in visited:
                continue
            visited.add(state)
            i = state.find('0')
            match i:
                case 0:
                    q.append((self.swap_chars(state, 0, 1), dist + 1))
                    q.append((self.swap_chars(state, 0, 3), dist + 1))
                case 1:
                    q.append((self.swap_chars(state, 1, 0), dist + 1))
                    q.append((self.swap_chars(state, 1, 2), dist + 1))
                    q.append((self.swap_chars(state, 1, 4), dist + 1))
                case 2:
                    q.append((self.swap_chars(state, 2, 1), dist + 1))
                    q.append((self.swap_chars(state, 2, 5), dist + 1))
                case 3:
                    q.append((self.swap_chars(state, 3, 0), dist + 1))
                    q.append((self.swap_chars(state, 3, 4), dist + 1))
                case 4:
                    q.append((self.swap_chars(state, 4, 1), dist + 1))
                    q.append((self.swap_chars(state, 4, 3), dist + 1))
                    q.append((self.swap_chars(state, 4, 5), dist + 1))
                case 5:
                    q.append((self.swap_chars(state, 5, 2), dist + 1))
                    q.append((self.swap_chars(state, 5, 4), dist + 1))
        return -1

    def swap_chars(self, word, i, j):
        word = list(word)
        word[i], word[j] = word[j], word[i]
        return ''.join(word)


s = Solution()
print(s.slidingPuzzle([[1, 2, 3], [4, 0, 5]]))
board = '123450'
