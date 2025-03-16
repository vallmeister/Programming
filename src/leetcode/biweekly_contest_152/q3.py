from collections import deque
from typing import List


class Solution:
    def longestCommonPrefix(self, words: List[str], k: int) -> List[int]:
        trie = {'#': 0, '*': ''}
        for word in words:
            curr_node = trie
            curr_node['#'] += 1
            for i, letter in enumerate(word):
                if letter not in curr_node:
                    curr_node[letter] = {'#': 0, '*': word[:i + 1]}
                curr_node = curr_node[letter]
                curr_node['#'] += 1
        n = len(words)
        ans = [0] * n
        prefixes = self.get_prefixes(trie, k)
        prefixes.sort(key=lambda x: (len(x[0]), -x[1]), reverse=True)
        for i in range(n):
            word = words[i]
            for prefix, freq in prefixes:
                if freq > k or not word.startswith(prefix):
                    ans[i] = len(prefix)
                    break
        return ans

    def get_prefixes(self, trie, k):
        q = deque()
        q.append((0, trie))
        ans = []
        while q:
            level, node = q.popleft()
            if node['#'] >= k:
                ans.append((node['*'], node['#']))
            else:
                continue
            for key in node.keys():
                if key in {'#', '*'}:
                    continue
                q.append((level + 1, node[key]))
        return ans


s = Solution()
print(s.longestCommonPrefix(words=["jump", "run", "run", "jump", "run"], k=2))
print(s.longestCommonPrefix(words=["dog", "racer", "car"], k=2))
