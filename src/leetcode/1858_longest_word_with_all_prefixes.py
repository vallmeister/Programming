from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = {'*': ''}
        for word in words:
            curr = trie
            for char in word:
                if char not in curr:
                    curr[char] = {}
                curr = curr[char]
            curr['*'] = word
        ans = ''

        def dfs(node):
            if '*' not in node:
                return

            nonlocal ans
            candidate = node['*']
            if len(candidate) > len(ans):
                ans = node['*']
            elif len(candidate) == len(ans):
                ans = min(ans, candidate)
            for child in node.keys():
                dfs(node[child])

        dfs(trie)
        return ans
