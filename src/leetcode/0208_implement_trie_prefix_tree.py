class TrieNode:

    def __init__(self):
        self.links = [None] * 26
        self.is_end = False

    def contains_key(self, ch):
        return self.links[ord(ch) - ord('a')] is not None

    def get(self, ch):
        return self.links[ord(ch) - ord('a')]

    def put(self, ch, node):
        self.links[ord(ch) - ord('a')] = node


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for curr_char in word:
            if not node.contains_key(curr_char):
                node.put(curr_char, TrieNode())
            node = node.get(curr_char)
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for curr_char in word:
            if node.contains_key(curr_char):
                node = node.get(curr_char)
            else:
                return False
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for curr_char in prefix:
            if node.contains_key(curr_char):
                node = node.get(curr_char)
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
