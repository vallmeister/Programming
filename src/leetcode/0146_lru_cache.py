class ListNode:
    def __init__(self, key=0, value=0, previous_node=None, next_node=None):
        self.key = key
        self.val = value
        self.prev = previous_node
        self.post = next_node


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.post = self.tail
        self.tail.prev = self.head

    def add_node(self, node):
        node.prev = self.head
        node.post = self.head.post

        node.prev.post = node
        node.post.prev = node

    def remove_node(self, node):
        node.prev.post = node.post
        node.post.prev = node.prev

    def move_node_to_head(self, node):
        self.remove_node(node)
        self.add_node(node)

    def pop_last_node(self):
        last = self.tail.prev
        self.remove_node(last)
        return last

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.move_node_to_head(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.move_node_to_head(node)
            node.val = value
        else:
            node = ListNode(key, value)
            self.add_node(node)
            self.cache[key] = node
            self.capacity -= 1

            if self.capacity < 0:
                last = self.pop_last_node()
                del self.cache[last.key]
                self.capacity += 1
