import random


class RandomizedSet:

    def __init__(self):
        self.ls = []
        self.elements = {}

    def insert(self, val: int) -> bool:
        if val in self.elements:
            return False
        self.elements[val] = len(self.ls)
        self.ls.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.elements:
            idx = self.elements[val]
            lst = self.ls[-1]
            self.ls[idx] = lst
            self.ls.pop()
            self.elements[lst] = idx
            del self.elements[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.ls)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()