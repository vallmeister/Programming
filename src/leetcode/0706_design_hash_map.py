class ListNode:

    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.next = None


class MyHashMap:

    def __init__(self):
        self.table = [-1] * 10 ** 4

    def _index(self, key):
        return key % 10 ** 4

    def put(self, key: int, value: int) -> None:
        idx = self._index(key)
        new_entry = ListNode(key, value)
        if self.table[idx] == -1:
            self.table[idx] = new_entry
        else:
            curr = self.table[idx]
            while curr.next:
                curr = curr.next
            curr.next = new_entry

    def get(self, key: int) -> int:
        entry = self.table[key]
        if entry == -1:
            return entry
        while entry:
            if entry.key == key:
                return entry.value
            elif entry.next:
                entry = entry.next
        return -1

# TODO: finish
    def remove(self, key: int) -> None:
        if self.table[key] != -1:
            entry = self.table[key]
            while entry:
                if entry.key == key:
                    pass

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
