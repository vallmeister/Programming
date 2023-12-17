from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])
        ans = []
        trie = {}
        for word in words:
            node = trie
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node['$'] = word

        def backtrack(row, col, curr_node):
            letter = board[row][col]
            if letter not in curr_node:
                return
            curr_node = curr_node[letter]
            if '$' in curr_node:
                ans.append(curr_node['$'])
                del curr_node['$']
            board[row][col] = '#'
            if row > 0:
                backtrack(row - 1, col, curr_node)
            if col > 0:
                backtrack(row, col - 1, curr_node)
            if row < m - 1:
                backtrack(row + 1, col, curr_node)
            if col < n - 1:
                backtrack(row, col + 1, curr_node)
            board[row][col] = letter

        for i in range(m):
            for j in range(n):
                backtrack(i, j, trie)
        return ans


s = Solution()
print(s.findWords([["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
                  words=["oath", "pea", "eat", "rain"]))
print(s.findWords([["a", "b"], ["c", "d"]], words=["abcb"]))
print(s.findWords([["a"]], ['a']))
