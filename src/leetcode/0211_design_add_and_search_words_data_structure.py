class TrieNode:

    def __init__(self):
        self.links = [None] * 26
        self.is_end = False

    def contains_key(self, letter):
        return self.links[ord(letter) - ord('a')] is not None

    def get(self, letter):
        return self.links[ord(letter) - ord('a')]

    def put(self, letter, node):
        self.links[ord(letter) - ord('a')] = node


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if not node.contains_key(char):
                node.put(char, TrieNode())
            node = node.get(char)
        node.is_end = True

    def search(self, word: str) -> bool:
        n = len(word)
        stack = [(self.root, 0)]
        while stack:
            node, i = stack.pop()
            if i == n:
                if node.is_end:
                    return True
                else:
                    continue
            char = word[i]
            if char == '.':
                for j in range(26):
                    key = chr(ord('a') + j)
                    if node.contains_key(key):
                        stack.append((node.get(key), i + 1))
            elif node.contains_key(char):
                stack.append((node.get(char), i + 1))
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
