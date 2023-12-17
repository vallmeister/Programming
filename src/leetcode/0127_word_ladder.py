from collections import deque, defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        words = defaultdict(set)
        word_to_wildcards = defaultdict(set)

        def get_wildcards(s):
            wildcards = set()
            for i in range(len(s)):
                wildcards.add(s[:i] + '*' + s[i+1:])
            return wildcards

        for word in wordList:
            wildcards = get_wildcards(word)
            for wildcard in wildcards:
                word_to_wildcards[word] = wildcards
                words[wildcard].add(word)
        word_to_wildcards[beginWord] = get_wildcards(beginWord)
        q = deque()
        q.append((beginWord, 1))
        visited = set()
        while q:
            word, distance = q.popleft()
            if word == endWord:
                return distance
            elif word in visited:
                continue
            visited.add(word)
            for wildcard in word_to_wildcards[word]:
                for descendant in words[wildcard]:
                    q.append((descendant, distance + 1))
        return 0


sol = Solution()
print(sol.ladderLength('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]))
print(sol.ladderLength('hit', 'cog', ["hot", "dot", "dog", "lot", "log"]))
