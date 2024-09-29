class Node:

    def __init__(self, freq, prev=None, nxt=None):
        self.freq = freq
        self.prev = prev
        self.next = nxt
        self.keys = set()


class AllOne:

    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}

    def inc(self, key: str) -> None:
        if key in self.map:
            node = self.map[key]
            freq = node.freq + 1
            node.keys.remove(key)

            next_node = node.next
            # insert new node
            if next_node.freq != freq:
                new_node = Node(freq, node, next_node)
                node.next = new_node
                next_node.prev = new_node
            next_node = node.next
            next_node.keys.add(key)
            self.map[key] = next_node
            if not node.keys:
                self.remove_node(node)
        else:
            if self.head.next.freq != 1:
                next_node = self.head.next
                new_node = Node(1, self.head, next_node)
                self.head.next = new_node
                next_node.prev = new_node
            node = self.head.next
            node.keys.add(key)
            self.map[key] = node

    def dec(self, key: str) -> None:
        pass

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))

    def remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node


print('Testcase #1')
obj = AllOne()
obj.inc("hello")
obj.inc("hello")
print(obj.getMaxKey())
print(obj.getMinKey())
obj.inc("leet")
print(obj.getMaxKey())
print(obj.getMinKey())

print('Testcase #14')
obj = AllOne()
obj.inc("a")
obj.inc("b")
obj.inc("b")
obj.inc("c")
obj.inc("c")
obj.inc("c")
obj.dec("b")
obj.dec("b")
print(obj.getMinKey())
obj.dec("a")
print(obj.getMaxKey())
print(obj.getMinKey())

print('Testcase #18')
obj = AllOne()
obj.inc("a")
obj.inc("b")
obj.inc("b")
obj.inc("b")
obj.inc("b")
obj.dec("b")
obj.dec("b")
print(obj.getMaxKey())
print(obj.getMinKey())
